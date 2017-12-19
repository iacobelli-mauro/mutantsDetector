import logging
from flask import current_app

class MutantDetector:
    matrix = None
    min_secuence_repeat = None
    mutant_genes = None
    dna_mutant_count = None
    min_mutant_dna_count = None

    def __init__(self, input_data):
        # Set from configuration the min secuence of chars,
        # the minimun count of dna and matrix values
        self.min_secuence_repeat = current_app.config['MIN_OCURRENCE_NEEDED']
        self.min_mutant_dna_count = current_app.config['MIN_MUTANT_DNA_COUNT']
        self.mutant_genes = []
        self.dna_mutant_count = 0
        # Load an set the matrix
        matrix_i = current_app.config['MATRIX_I_LENGTH']
        matrix_x = current_app.config['MATRIX_X_LENGTH']
        self.matrix = [[0 for y in xrange(matrix_i)] for x in xrange(matrix_x)]
        for index, row in enumerate(input_data):
            adn_data = list(row)
            for adn_index, value in enumerate(adn_data):
                self.matrix[index][adn_index] = value

    def __add_genes(self, genes):
        # Add the genes to the temporal list, to avoid repetition
        self.mutant_genes.extend(genes)
        # Add one to the mutant dna finded
        self.dna_mutant_count = self.dna_mutant_count + 1

    def __horizontal_check(self, pos_x, pos_i, value):
        # Check for horizontal ocurrences
        max_position_to_check_axis_x = pos_i + (self.min_secuence_repeat - 1)
        equality_count = 1
        # Check if the final required position with the same value, exists
        if max_position_to_check_axis_x < len(self.matrix[pos_x]):
            logging.debug("Horizontal Check")
            # Genes to be saved in case of the repetition of bases
            unchecked_genes = []
            unchecked_genes.append(str(pos_x) + "-" + str(pos_i))
            # Check if the values exists in inverse order
            for check_pos in xrange(max_position_to_check_axis_x, pos_i, -1):
                gene_position = str(pos_x) + "-" + str(check_pos)
                unchecked_genes.append(gene_position)
                logging.debug("Checking %s", gene_position)
                # Check if value is the same and the gene is not with another group
                if(value == self.matrix[pos_x][check_pos]
                   and gene_position not in self.mutant_genes):
                    equality_count = equality_count + 1
                else:
                    return False
            if equality_count == self.min_secuence_repeat:
                self.__add_genes(unchecked_genes)
                return True
            else:
                return False

    def __vertical_check(self, pos_x, pos_i, value):
        # Check for vertical ocurrences
        max_position_to_check_axis_i = pos_x + (self.min_secuence_repeat - 1)
        equality_count = 1
        # Check if the final required position with the same value, exists
        if max_position_to_check_axis_i < len(self.matrix):
            logging.debug("Vertical Check")
            # Genes to be saved in case of the repetition of bases
            unchecked_genes = []
            unchecked_genes.append(str(pos_x) + "-" + str(pos_i))
            # Check if the values exists in inverse order
            for check_pos in xrange(max_position_to_check_axis_i, pos_x, -1):
                gene_position = str(check_pos) + "-" + str(pos_i)
                unchecked_genes.append(gene_position)
                logging.debug("Checking %s", gene_position)
                # Check if value is the same and the gene is not with another group
                if (value == self.matrix[check_pos][pos_i]
                        and gene_position not in self.mutant_genes):
                    equality_count = equality_count + 1
                else:
                    return False
            if equality_count == self.min_secuence_repeat:
                self.__add_genes(unchecked_genes)
                return True
            else:
                return False

    def __diagonal_up_check(self, pos_x, pos_i, value):
        # Check for diagonal Up ocurrences
        equality_count = 1
        max_position_to_check_axis_i = pos_x + (self.min_secuence_repeat - 1)
        max_position_to_check_axis_x = pos_i + (self.min_secuence_repeat - 1)
        # Check if the final required position with the same value, exists
        if (max_position_to_check_axis_i < len(self.matrix)
                and max_position_to_check_axis_x <
                len(self.matrix[max_position_to_check_axis_i])):
            logging.debug("Diagonal Check")
            # Genes to be saved in case of the repetition of bases
            unchecked_genes = []
            unchecked_genes.append(str(pos_x) + "-" + str(pos_i))
            # Check if the values exists in inverse order
            for check_pos in xrange(self.min_secuence_repeat - 1, 0, -1):
                gene_position = str(pos_x + check_pos) + "-" + str(pos_i + check_pos)
                unchecked_genes.append(gene_position)
                logging.debug("Checking %s", gene_position)
                # Check if value is the same and the gene is not with another group
                if (value == self.matrix[pos_x + check_pos][pos_i + check_pos]
                        and gene_position not in self.mutant_genes):
                    equality_count = equality_count + 1
                else:
                    return False
            if equality_count == self.min_secuence_repeat:
                self.__add_genes(unchecked_genes)
                return True
            else:
                return False

    def __diagonal_down_check(self, pos_x, pos_i, value):
        # Check for diagonal down ocurrences
        equality_count = 1
        min_position_to_check_axis_x = pos_i - (self.min_secuence_repeat - 1)
        max_position_to_check_axis_i = pos_x + (self.min_secuence_repeat - 1)
        # Check if the final required position with the same value, exists
        if (max_position_to_check_axis_i < len(self.matrix)
                and min_position_to_check_axis_x >= 0):
            logging.debug("Diagonal inverse Check")
            # Genes to be saved in case of the repetition of bases
            unchecked_genes = []
            unchecked_genes.append(str(pos_x) + "-" + str(pos_i))
            # Check if the values exists in inverse order
            for check_pos in xrange(self.min_secuence_repeat - 1, 0, -1):
                gene_position = str(pos_x + check_pos) + "-" + str(pos_i + check_pos)
                unchecked_genes.append(gene_position)
                logging.debug("Checking %s", gene_position)
                # Check if value is the same and the gene is not with another group
                if (value == self.matrix[pos_x + check_pos][pos_i - check_pos]
                        and gene_position not in self.mutant_genes):
                    equality_count = equality_count + 1
                else:
                    return False
            if equality_count == self.min_secuence_repeat:
                self.__add_genes(unchecked_genes)
                return True
            else:
                return False

    def is_mutant_dna(self):
        # Search in the matrix for the ocurrences
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                gene_position = str(i) + "-" + str(j)
                # If the gene is already in a group, is in vain to search
                if gene_position in self.mutant_genes:
                    break
                value = self.matrix[i][j]
                logging.debug("Muestra %s", gene_position)
                # In any case, if a group is finded, loop to the next position
                if self.__horizontal_check(i, j, value):
                    break
                if self.__vertical_check(i, j, value):
                    break
                if self.__diagonal_up_check(i, j, value):
                    break
                if self.__diagonal_down_check(i, j, value):
                    break
        #Debug log data
        logging.debug("Checkeo finalizado")
        logging.debug("Adn Mutante: %s", str(self.dna_mutant_count))
        for row in self.matrix:
            logging.debug(row)
        logging.debug(self.mutant_genes)
        return self.dna_mutant_count > self.min_mutant_dna_count
