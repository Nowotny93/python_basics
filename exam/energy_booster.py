fruit = input()
size_set = input()
number_sets = int(input())

if fruit == "Watermelon" and size_set == "big":
    price_big_watermelon = (5 * 28.70) * number_sets
    price = price_big_watermelon
elif fruit == "Watermelon" and size_set == "small":
    price_small_watermelon = (2 * 56) * number_sets
    price = price_small_watermelon
elif fruit == "Mango" and size_set == "big":
    price_big_mango = (5 * 19.60) * number_sets
    price = price_big_mango
elif fruit == "Mango" and size_set == "small":
    price_small_mango = (2 * 36.66) * number_sets
    price = price_small_mango
elif fruit == "Pineapple" and size_set == "big":
    price_big_pineapple = (5 * 24.80) * number_sets
    price = price_big_pineapple
elif fruit == "Pineapple" and size_set == "small":
    price_small_pineapple = (2 * 42.10) * number_sets
    price = price_small_pineapple
elif fruit == "Raspberry" and size_set == "big":
    price_big_raspberry = (5 * 15.20) * number_sets
    price = price_big_raspberry
elif fruit == "Raspberry" and size_set == "small":
    price_small_raspberry = (2 * 20) * number_sets
    price = price_small_raspberry

if 400 <= price <= 1000:
    end_price = price - price * 0.15
    print(f'{end_price:.2f} lv.')
elif price > 1000:
    end_price = price - price * 0.5
    print(f'{end_price:.2f} lv.')
else:
    print(f'{price:.2f} lv.')


