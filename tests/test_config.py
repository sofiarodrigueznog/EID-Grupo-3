#Test para el archivo config.py

import unittest

from scenes import config as cfg


class TestConfig(unittest.TestCase):

    def test_funcion(self):
        self.assertEqual(cfg.f(0), 1)
        self.assertEqual(cfg.f(1), 2)
        self.assertEqual(cfg.f(2), 5)

    def test_intervalo(self):
        self.assertEqual(cfg.a, 0.0)
        self.assertEqual(cfg.b, 2.0)

    def test_valores_n(self):
        self.assertEqual(
            cfg.n_values,
            [4, 8, 16, 32]
        )

    def test_muestreo(self):
        self.assertEqual(
            cfg.sample_type,
            "center"
        )

    def test_delta_x(self):
        esperados = [0.5, 0.25, 0.125, 0.0625]

        for n, esperado in zip(
            cfg.n_values, esperados
        ):
            self.assertAlmostEqual(
                cfg.delta_x(n),
                esperado
            )

    def test_puntos_medios(self):
        esperados = [0.25, 0.75, 1.25, 1.75]

        obtenidos = [
            cfg.sample_x(i, 4)
            for i in range(4)
        ]

        for obtenido, esperado in zip(
            obtenidos, esperados
        ):
            self.assertAlmostEqual(
                obtenido, esperado
            )

    def test_sumas_riemann(self):
        resultados = {
            4: 4.625,
            8: 4.65625,
            16: 4.6640625,
            32: 4.666015625,
        }

        for n, esperado in resultados.items():

            suma = sum(
                cfg.f(cfg.sample_x(i, n))
                * cfg.delta_x(n)
                for i in range(n)
            )

            self.assertAlmostEqual(
                suma, esperado, places=10
            )

    def test_formula_general(self):
        for n in cfg.n_values:

            suma = sum(
                cfg.f(cfg.sample_x(i, n))
                * cfg.delta_x(n)
                for i in range(n)
            )

            formula = 14 / 3 - 2 / (3 * n**2)

            self.assertAlmostEqual(
                suma, formula, places=10
            )

    def test_parametros_invalidos(self):
        with self.assertRaises(ValueError):
            cfg.delta_x(0)

        with self.assertRaises(ValueError):
            cfg.sample_x(4, 4)


if __name__ == "__main__":
    unittest.main()
