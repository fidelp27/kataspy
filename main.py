from sheep_count import count_sheeps


def main():
  sheep_array = [
      True, True, True, False,
      True, True, True, True,
      True, False, True, False,
      True, False, False, True,
      True, True, True, True,
      False, False, True, True
  ]
  count_sheeps(sheep_array)
if __name__ == "__main__":
  main()
  