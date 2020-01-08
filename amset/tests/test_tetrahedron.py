import numpy as np
import unittest

from amset.tetrahedron import TetrahedralBandStructure, get_cross_section_values
from pymatgen import Spin


class TetrahedralBandStructureTest(unittest.TestCase):
    def setUp(self):
        self.kpoints = np.array(
            [
                [0.0, 0.0, 0.0],
                [-0.5, 0.0, 0.0],
                [0.0, -0.5, 0.0],
                [-0.5, -0.5, 0.0],
                [0.0, 0.0, -0.5],
                [-0.5, 0.0, -0.5],
                [0.0, -0.5, -0.5],
                [-0.5, -0.5, -0.5],
            ]
        )

        # self.energies = {Spin.up: np.array([[0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]])}
        # self.energies = {Spin.up: np.array([[0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8, 9]])}
        # self.energies = {Spin.up: np.array([[1, 2, 3, 4, 5, 6, 7, 8]])}
        # self.energies = {Spin.up: np.array([[0, 1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 0]])}
        # self.energies = {Spin.up: np.array([[0, 1, 2, 3, 4, 5, 6, 7]])}
        self.energies = {Spin.up: np.array([[1, 2, 2, 2, 2, 2, 2, 3]])}

        self.tetrahedra = np.array(
            [
                [0, 1, 3, 7],
                [0, 1, 5, 7],
                [0, 2, 3, 7],
                [0, 2, 6, 7],
                [0, 4, 5, 7],
                [0, 4, 6, 7],
                [1, 0, 2, 6],
                [1, 0, 4, 6],
                [1, 3, 2, 6],
                [1, 3, 7, 6],
                [1, 5, 4, 6],
                [1, 5, 7, 6],
                [2, 3, 1, 5],
                [2, 3, 7, 5],
                [2, 0, 1, 5],
                [2, 0, 4, 5],
                [2, 6, 7, 5],
                [2, 6, 4, 5],
                [3, 2, 0, 4],
                [3, 2, 6, 4],
                [3, 1, 0, 4],
                [3, 1, 5, 4],
            ]
        )

    def test_test_init(self):
        tbs = TetrahedralBandStructure(self.energies, self.kpoints, self.tetrahedra)

        # print(tbs.tetrahedra[Spin.up])
        # print(tbs.tetrahedra[Spin.up][0, 0])
        # print(tbs.tetrahedra_energies[Spin.up])
        # print(tbs.max_tetrahedra_energies)
        # print(tbs.min_tetrahedra_energies)
        # print(tbs.e21)
        # print(tbs.get_intersecting_tetrahedra(Spin.up, 0))
        # print(tbs.get_tetrahedra_density_of_states(Spin.up, 2.5))
        # print(tbs.get_tetrahedra_density_of_states(Spin.up, 6.5)[0])
        # print(tbs._tetrahedron_volume)
        # print(tbs._tetrahedron_volume * 0.0357142)
        # print(tbs._tetrahedron_volume * 0.2589285714)
        # print(tbs._tetrahedron_volume * 0.004464285714)
        # print(tbs.get_tetrahedra_density_of_states(Spin.up, 4.5))

        # dos, tet_mask, contrib = tbs.get_tetrahedra_density_of_states(
        #     Spin.up, 6.5, return_contributions=True)
        # tetrahedra = tbs.tetrahedra[Spin.up][tet_mask]

        # avg_kdiff = get_cross_section_values(self.kpoints[tetrahedra], *contrib)
        # print(avg_kdiff[0])

        # density of states seems OK!