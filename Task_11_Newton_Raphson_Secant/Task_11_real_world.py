from scipy.optimize import root_scalar

# Investment Return Analysis
# Find the rate of return (IRR) that makes NPV = 0

cash_flows = [-50000, 12000, 15000, 18000, 20000]

def npv(rate):
    return sum(
        cf / (1 + rate) ** t
        for t, cf in enumerate(cash_flows)
    )

def d_npv(rate):
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant Method: {secant.root:.6%}")
print(f"NPV at IRR: {npv(newton.root):.6f}")