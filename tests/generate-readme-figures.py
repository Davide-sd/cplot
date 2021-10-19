import matplotlib.pyplot as plt
import mpmath
import numpy as np
import scipy.special
import scipyx as spx

import cplot

# gray to improve visibility on github's dark background
_gray = "#969696"
style = {
    "text.color": _gray,
    "axes.labelcolor": _gray,
    "axes.edgecolor": _gray,
    "xtick.color": _gray,
    "ytick.color": _gray,
}
plt.style.use(style)


def riemann_zeta(z):
    z = np.asarray(z)
    z_shape = z.shape
    vals = [mpmath.zeta(val) for val in z.flatten()]
    return np.array([float(val.real) + 1j * float(val.imag) for val in vals]).reshape(
        z_shape
    )


def riemann_xi(z):
    # https://en.wikipedia.org/wiki/Riemann_Xi_function
    return (
        0.5
        * z
        * (z - 1)
        * np.pi ** (-z / 2)
        * scipy.special.gamma(z / 2)
        * riemann_zeta(z)
    )


def riemann_siegel_z(z):
    z = np.asarray(z)
    z_shape = z.shape
    vals = [mpmath.siegelz(val) for val in z.flatten()]
    return np.array([float(val.real) + 1j * float(val.imag) for val in vals]).reshape(
        z_shape
    )


def riemann_siegel_theta(z):
    z = np.asarray(z)
    z_shape = z.shape
    vals = [mpmath.siegeltheta(val) for val in z.flatten()]
    return np.array([float(val.real) + 1j * float(val.imag) for val in vals]).reshape(
        z_shape
    )


def f(z):
    return (z ** 2 - 1) * (z - 2 - 1j) ** 2 / (z ** 2 + 2 + 2j)


n = 201
for name in ["cam16", "cielab", "oklab", "hsl"]:
    cplot.plot(f, (-3, +3, n), (-3, +3, n), colorspace=name, add_colorbars=False)
    plt.savefig(f"{name}-10.svg", transparent=True, bbox_inches="tight")
    plt.close()
    #
    cplot.plot(
        f,
        (-3, +3, n),
        (-3, +3, n),
        colorspace=name,
        abs_scaling=lambda x: np.sqrt(x) / (np.sqrt(x) + 1),
        add_colorbars=False,
    )
    plt.savefig(f"{name}-05.svg", transparent=True, bbox_inches="tight")
    plt.close()
    #
    cplot.plot(
        f,
        (-3, +3, n),
        (-3, +3, n),
        colorspace=name,
        abs_scaling=lambda x: np.full_like(x, 0.5),
        add_colorbars=False,
    )
    plt.savefig(f"{name}-00.svg", transparent=True, bbox_inches="tight")
    plt.close()


# First function from the SIAM-100-digit challenge
# <https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems>
n = 401
cplot.plot(
    lambda z: np.cos(np.log(z) / z) / z,
    (-1, 1, n),
    (-1, 1, n),
    abs_scaling=lambda x: np.sqrt(x) / (np.sqrt(x) + 1),
)
plt.savefig("siam.svg", transparent=True, bbox_inches="tight")
plt.close()

n = 400
cplot.plot(lambda z: np.sin(z ** 3) / z, (-2, 2, n), (-2, 2, n))
plt.savefig("sinz3z.svg", transparent=True, bbox_inches="tight")
plt.close()

args = [
    #
    ("z1.svg", lambda z: z ** 1, (-2, +2), (-2, +2)),
    ("z2.svg", lambda z: z ** 2, (-2, +2), (-2, +2)),
    ("z3.svg", lambda z: z ** 3, (-2, +2), (-2, +2)),
    #
    ("1z.svg", lambda z: 1 / z, (-2.0, +2.0), (-2.0, +2.0)),
    ("z-absz.svg", lambda z: z / np.abs(z), (-2, +2), (-2, +2)),
    ("z+1-z-1.svg", lambda z: (z + 1) / (z - 1), (-5, +5), (-5, +5)),
    # roots of unity
    ("z6+1.svg", lambda z: z ** 6 + 1, (-1.5, 1.5), (-1.5, 1.5)),
    ("z6-1.svg", lambda z: z ** 6 - 1, (-1.5, 1.5), (-1.5, 1.5)),
    ("z-6+1.svg", lambda z: z ** (-6) + 1, (-1.5, 1.5), (-1.5, 1.5)),
    #
    ("zz.svg", lambda z: z ** z, (-3, +3), (-3, +3)),
    ("1zz.svg", lambda z: (1 / z) ** z, (-3, +3), (-3, +3)),
    ("z1z.svg", lambda z: z ** (1 / z), (-3, +3), (-3, +3)),
    #
    ("root2.svg", np.sqrt, (-2, +2), (-2, +2)),
    ("root3.svg", lambda x: x ** (1 / 3), (-2, +2), (-2, +2)),
    ("root4.svg", lambda x: x ** 0.25, (-2, +2), (-2, +2)),
    #
    ("log.svg", np.log, (-2, +2), (-2, +2)),
    ("exp.svg", np.exp, (-3, +3), (-3, +3)),
    ("exp2.svg", np.exp2, (-3, +3), (-3, +3)),
    # essential singularities
    ("exp1z.svg", lambda z: np.exp(1 / z), (-1, +1), (-1, +1)),
    ("zsin1z.svg", lambda z: z * np.sin(1 / z), (-0.6, +0.6), (-0.6, +0.6)),
    ("1cosz.svg", lambda z: 1 / np.cos(z), (-0.6, +0.6), (-0.6, +0.6)),
    #
    ("exp-z2.svg", lambda z: np.exp(-(z ** 2)), (-3, +3), (-3, +3)),
    ("11z2.svg", lambda z: 1 / (1 + z ** 2), (-3, +3), (-3, +3)),
    ("erf.svg", scipy.special.erf, (-3, +3), (-3, +3)),
    #
    ("sin.svg", np.sin, (-5, +5), (-5, +5)),
    ("cos.svg", np.cos, (-5, +5), (-5, +5)),
    ("tan.svg", np.tan, (-5, +5), (-5, +5)),
    #
    ("sinh.svg", np.sinh, (-5, +5), (-5, +5)),
    ("cosh.svg", np.cosh, (-5, +5), (-5, +5)),
    ("tanh.svg", np.tanh, (-5, +5), (-5, +5)),
    #
    ("arcsin.svg", np.arcsin, (-2, +2), (-2, +2)),
    ("arccos.svg", np.arccos, (-2, +2), (-2, +2)),
    ("arctan.svg", np.arctan, (-2, +2), (-2, +2)),
    #
    ("sinz-z.svg", lambda z: np.sin(z) / z, (-7, +7), (-7, +7)),
    ("cosz-z.svg", lambda z: np.cos(z) / z, (-7, +7), (-7, +7)),
    ("tanz-z.svg", lambda z: np.tan(z) / z, (-7, +7), (-7, +7)),
    #
    ("gamma.svg", scipy.special.gamma, (-5, +5), (-5, +5)),
    ("digamma.svg", scipy.special.digamma, (-5, +5), (-5, +5)),
    ("zeta.svg", riemann_zeta, (-30, +30), (-30, +30)),
    # ("airy.svg", scipy.special.airy, (-5, +5), (-5, +5)),  # TODO not working?!
    #
    ("riemann-xi.svg", riemann_xi, (-20, +20), (-20, +20)),
    ("riemann-siegel-z.svg", riemann_siegel_z, (-20, +20), (-20, +20)),
    ("riemann-siegel-theta.svg", riemann_siegel_theta, (-20, +20), (-20, +20)),
    #
    # jacobian elliptic functions
    ("ellipj-sn-06.svg", lambda z: spx.ellipj(z, 0.6)[0], (-6, +6), (-6, +6)),
    ("ellipj-cn-06.svg", lambda z: spx.ellipj(z, 0.6)[1], (-6, +6), (-6, +6)),
    ("ellipj-dn-06.svg", lambda z: spx.ellipj(z, 0.6)[2], (-6, +6), (-6, +6)),
    #
    ("lambertw.svg", scipy.special.lambertw, (-5, +5), (-5, +5)),
    # https://www.dynamicmath.xyz
    (
        "some-polynomial.svg",
        lambda z: 0.926 * (z + 7.3857e-2 * z ** 5 + 4.5458e-3 * z ** 9),
        (-3, 3),
        (-3, 3),
    ),
    # non-analytic
    (
        "non-analytic.svg",
        lambda z: np.imag(np.exp(-1j * np.pi / 4) * z ** n)
        + 1j * np.imag(np.exp(1j * np.pi / 4) * (z - 1) ** 4),
        (-2.0, +3.0),
        (-2.0, +3.0),
    ),
]
for filename, fun, x, y in args:
    cplot.plot(fun, (x[0], x[1], n), (y[0], y[1], n), add_colorbars=False)
    plt.savefig(filename, transparent=True, bbox_inches="tight")
    plt.close()
