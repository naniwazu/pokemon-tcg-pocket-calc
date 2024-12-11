def oak_to_pokeball(m, n):
    return (m**2 + 2 * n**2 - m - 2 * n) / (m * n * (n - 1))


def pokeball_to_oak(m, n):
    return (2 * m + n - 3) / (m * (n - 1))


for n in range(5, 15):
    for m in range(3, n + 1):
        print(f"n={n}, m={m}:")
        print(f"owk → pokeball: {oak_to_pokeball(m, n)*100:.2f}%")
        print(f"pokeball → owk: {pokeball_to_oak(m, n)*100:.2f}%")
        print(
            f"difference: {(oak_to_pokeball(m, n) - pokeball_to_oak(m, n))*100:.2f}%\n"
        )

"""
n=5, m=3:
owk → pokeball: 76.67%
pokeball → owk: 66.67%
difference: 10.00%

n=5, m=4:
owk → pokeball: 65.00%
pokeball → owk: 62.50%
difference: 2.50%

n=5, m=5:
owk → pokeball: 60.00%
pokeball → owk: 60.00%
difference: 0.00%

n=6, m=3:
owk → pokeball: 73.33%
pokeball → owk: 60.00%
difference: 13.33%

n=6, m=4:
owk → pokeball: 60.00%
pokeball → owk: 55.00%
difference: 5.00%

n=6, m=5:
owk → pokeball: 53.33%
pokeball → owk: 52.00%
difference: 1.33%

n=6, m=6:
owk → pokeball: 50.00%
pokeball → owk: 50.00%
difference: 0.00%

n=7, m=3:
owk → pokeball: 71.43%
pokeball → owk: 55.56%
difference: 15.87%

n=7, m=4:
owk → pokeball: 57.14%
pokeball → owk: 50.00%
difference: 7.14%

n=7, m=5:
owk → pokeball: 49.52%
pokeball → owk: 46.67%
difference: 2.86%

n=7, m=6:
owk → pokeball: 45.24%
pokeball → owk: 44.44%
difference: 0.79%

n=7, m=7:
owk → pokeball: 42.86%
pokeball → owk: 42.86%
difference: 0.00%

n=8, m=3:
owk → pokeball: 70.24%
pokeball → owk: 52.38%
difference: 17.86%

n=8, m=4:
owk → pokeball: 55.36%
pokeball → owk: 46.43%
difference: 8.93%

n=8, m=5:
owk → pokeball: 47.14%
pokeball → owk: 42.86%
difference: 4.29%

n=8, m=6:
owk → pokeball: 42.26%
pokeball → owk: 40.48%
difference: 1.79%

n=8, m=7:
owk → pokeball: 39.29%
pokeball → owk: 38.78%
difference: 0.51%

n=8, m=8:
owk → pokeball: 37.50%
pokeball → owk: 37.50%
difference: 0.00%

n=9, m=3:
owk → pokeball: 69.44%
pokeball → owk: 50.00%
difference: 19.44%

n=9, m=4:
owk → pokeball: 54.17%
pokeball → owk: 43.75%
difference: 10.42%

n=9, m=5:
owk → pokeball: 45.56%
pokeball → owk: 40.00%
difference: 5.56%

n=9, m=6:
owk → pokeball: 40.28%
pokeball → owk: 37.50%
difference: 2.78%

n=9, m=7:
owk → pokeball: 36.90%
pokeball → owk: 35.71%
difference: 1.19%

n=9, m=8:
owk → pokeball: 34.72%
pokeball → owk: 34.38%
difference: 0.35%

n=9, m=9:
owk → pokeball: 33.33%
pokeball → owk: 33.33%
difference: 0.00%

n=10, m=3:
owk → pokeball: 68.89%
pokeball → owk: 48.15%
difference: 20.74%

n=10, m=4:
owk → pokeball: 53.33%
pokeball → owk: 41.67%
difference: 11.67%

n=10, m=5:
owk → pokeball: 44.44%
pokeball → owk: 37.78%
difference: 6.67%

n=10, m=6:
owk → pokeball: 38.89%
pokeball → owk: 35.19%
difference: 3.70%

n=10, m=7:
owk → pokeball: 35.24%
pokeball → owk: 33.33%
difference: 1.90%

n=10, m=8:
owk → pokeball: 32.78%
pokeball → owk: 31.94%
difference: 0.83%

n=10, m=9:
owk → pokeball: 31.11%
pokeball → owk: 30.86%
difference: 0.25%

n=10, m=10:
owk → pokeball: 30.00%
pokeball → owk: 30.00%
difference: 0.00%

n=11, m=3:
owk → pokeball: 68.48%
pokeball → owk: 46.67%
difference: 21.82%

n=11, m=4:
owk → pokeball: 52.73%
pokeball → owk: 40.00%
difference: 12.73%

n=11, m=5:
owk → pokeball: 43.64%
pokeball → owk: 36.00%
difference: 7.64%

n=11, m=6:
owk → pokeball: 37.88%
pokeball → owk: 33.33%
difference: 4.55%

n=11, m=7:
owk → pokeball: 34.03%
pokeball → owk: 31.43%
difference: 2.60%

n=11, m=8:
owk → pokeball: 31.36%
pokeball → owk: 30.00%
difference: 1.36%

n=11, m=9:
owk → pokeball: 29.49%
pokeball → owk: 28.89%
difference: 0.61%

n=11, m=10:
owk → pokeball: 28.18%
pokeball → owk: 28.00%
difference: 0.18%

n=11, m=11:
owk → pokeball: 27.27%
pokeball → owk: 27.27%
difference: 0.00%

n=12, m=3:
owk → pokeball: 68.18%
pokeball → owk: 45.45%
difference: 22.73%

n=12, m=4:
owk → pokeball: 52.27%
pokeball → owk: 38.64%
difference: 13.64%

n=12, m=5:
owk → pokeball: 43.03%
pokeball → owk: 34.55%
difference: 8.48%

n=12, m=6:
owk → pokeball: 37.12%
pokeball → owk: 31.82%
difference: 5.30%

n=12, m=7:
owk → pokeball: 33.12%
pokeball → owk: 29.87%
difference: 3.25%

n=12, m=8:
owk → pokeball: 30.30%
pokeball → owk: 28.41%
difference: 1.89%

n=12, m=9:
owk → pokeball: 28.28%
pokeball → owk: 27.27%
difference: 1.01%

n=12, m=10:
owk → pokeball: 26.82%
pokeball → owk: 26.36%
difference: 0.45%

n=12, m=11:
owk → pokeball: 25.76%
pokeball → owk: 25.62%
difference: 0.14%

n=12, m=12:
owk → pokeball: 25.00%
pokeball → owk: 25.00%
difference: 0.00%

n=13, m=3:
owk → pokeball: 67.95%
pokeball → owk: 44.44%
difference: 23.50%

n=13, m=4:
owk → pokeball: 51.92%
pokeball → owk: 37.50%
difference: 14.42%

n=13, m=5:
owk → pokeball: 42.56%
pokeball → owk: 33.33%
difference: 9.23%

n=13, m=6:
owk → pokeball: 36.54%
pokeball → owk: 30.56%
difference: 5.98%

n=13, m=7:
owk → pokeball: 32.42%
pokeball → owk: 28.57%
difference: 3.85%

n=13, m=8:
owk → pokeball: 29.49%
pokeball → owk: 27.08%
difference: 2.40%

n=13, m=9:
owk → pokeball: 27.35%
pokeball → owk: 25.93%
difference: 1.42%

n=13, m=10:
owk → pokeball: 25.77%
pokeball → owk: 25.00%
difference: 0.77%

n=13, m=11:
owk → pokeball: 24.59%
pokeball → owk: 24.24%
difference: 0.35%

n=13, m=12:
owk → pokeball: 23.72%
pokeball → owk: 23.61%
difference: 0.11%

n=13, m=13:
owk → pokeball: 23.08%
pokeball → owk: 23.08%
difference: 0.00%

n=14, m=3:
owk → pokeball: 67.77%
pokeball → owk: 43.59%
difference: 24.18%

n=14, m=4:
owk → pokeball: 51.65%
pokeball → owk: 36.54%
difference: 15.11%

n=14, m=5:
owk → pokeball: 42.20%
pokeball → owk: 32.31%
difference: 9.89%

n=14, m=6:
owk → pokeball: 36.08%
pokeball → owk: 29.49%
difference: 6.59%

n=14, m=7:
owk → pokeball: 31.87%
pokeball → owk: 27.47%
difference: 4.40%

n=14, m=8:
owk → pokeball: 28.85%
pokeball → owk: 25.96%
difference: 2.88%

n=14, m=9:
owk → pokeball: 26.62%
pokeball → owk: 24.79%
difference: 1.83%

n=14, m=10:
owk → pokeball: 24.95%
pokeball → owk: 23.85%
difference: 1.10%

n=14, m=11:
owk → pokeball: 23.68%
pokeball → owk: 23.08%
difference: 0.60%

n=14, m=12:
owk → pokeball: 22.71%
pokeball → owk: 22.44%
difference: 0.27%

n=14, m=13:
owk → pokeball: 21.98%
pokeball → owk: 21.89%
difference: 0.08%

n=14, m=14:
owk → pokeball: 21.43%
pokeball → owk: 21.43%
difference: 0.00%

"""
