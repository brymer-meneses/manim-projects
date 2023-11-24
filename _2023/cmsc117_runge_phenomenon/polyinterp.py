import numpy as np

def LagrangeInterpolation(f, a, b, step):
  xs = np.array(range(a, b, step), float)

  def lnk(x, k):
    res = 1
    for i, x_i in enumerate(xs):
      if i == k: pass
      res *= (x - x_i) / (xs[k] - x_i)
    return res

  for i in range(len(xs)):
    print(lnk(1, i))

  # def p(x):
  #   res = 0
  #   for k, node in enumerate(xs):
  #     res += f(node) * lnk(x, k)
  #   return res
  # return p

if __name__ == "__main__":
  f = lambda x: x**2
  p = LagrangeInterpolation(f, 1, 10, 1)
  print(p(5))