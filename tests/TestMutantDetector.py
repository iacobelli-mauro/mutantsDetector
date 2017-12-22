#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from mutantsDetector.services.MutantDetectorService import MutantDetector


class TestMutantDetector(unittest.TestCase):
    """Test unit class for the Mutan Detector."""
    horizontal_mutant_test_case = [
        "AAAATT", "CCGTAT", "GCTCCC", "TCGTAT", "GGTGAC", "ACTTTT"]
    horizontal_human_test_case = [
        "AAAATT", "CCGTAT", "GCTCCC", "TCGTAT", "GGTGAC", "ACTGGT"]

    vertical_mutant_test_case = ["CGGATT", "CGGTAG",
                                 "GGTCCT", "TGATAT", "GGTGAT", "ACTGGT"]
    vertical_human_test_case = ["CGGATT", "CGGTAG",
                                "GTTCCT", "TGATAT", "GTTGAG", "ACTGGT"]

    diagonal_mutant_test_case = ["CGGATT", "CCGTAG",
                                 "GTCGCT", "TGACGT", "GTTGAG", "ACTGGT"]
    diagonal_human_test_case = ["CGGATT", "CCATAG",
                                "GTCGCT", "TGACAT", "GTTGCG", "ACTGGT"]

    inverse_diagonal_mutant_test_case = [
        "CGGGTA", "CCGTAG", "GGCACT", "GGACAT", "GTTGCG", "ACTGGT"]
    inverse_diagonal_human_test_case = [
        "CGGTTA", "CAATAG", "GCCACT", "GGACAT", "GATGCG", "ACTGGT"]

    def test_horizontal_mutant(self):
        """ Método para validar la deteccion de un Mutante
           de manera Horizonta en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.horizontal_mutant_test_case)
        self.assertTrue(md_service.is_mutant_dna())

    def test_horizontal_human(self):
        """ Método para validar la deteccion de un Humano
           de manera Horizonta en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.horizontal_human_test_case)
        self.assertFalse(md_service.is_mutant_dna())

    def test_vertical_mutant(self):
        """ Método para validar la deteccion de un Mutante
           de manera Vertical en el servicio de detección de mutantes"""
        md_service = MutantDetector(self.vertical_mutant_test_case)
        self.assertTrue(md_service.is_mutant_dna())

    def test_vertical_human(self):
        """ Método para validar la deteccion de un Humano
           de manera Vertical en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.vertical_human_test_case)
        self.assertFalse(md_service.is_mutant_dna())

    def test_diagonal_mutant(self):
        """ Método para validar la deteccion de un Mutante
           de manera Diagonal en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.diagonal_mutant_test_case)
        self.assertTrue(md_service.is_mutant_dna())

    def test_diagonal_human(self):
        """ Método para validar la deteccion de un Humano
           de manera Diagonal en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.diagonal_human_test_case)
        self.assertFalse(md_service.is_mutant_dna())

    def test_inverse_diagonal_mutant(self):
        """ Método para validar la deteccion de un Mutante
           de manera Diagonal inversa en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.inverse_diagonal_mutant_test_case)
        self.assertTrue(md_service.is_mutant_dna())

    def test_inverse_diagonal_human(self):
        """ Método para validar la deteccion de un Humano
           de manera Diagonal inversa en el
           servicio de detección de mutantes"""
        md_service = MutantDetector(self.inverse_diagonal_human_test_case)
        self.assertFalse(md_service.is_mutant_dna())

