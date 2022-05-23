nylon_num = int(input())
paint_num = int(input())
razreditel_num = int(input())
work_time = int(input())

nylon_price = (nylon_num + 2) * 1.50
paint_price = (paint_num * 1.10 ) * 14.50
razreditel_price = razreditel_num * 5.00
bag_price = 0.40

materiali_total_price = nylon_price + paint_price + razreditel_price + bag_price
workers_price = materiali_total_price * 0.30 * work_time
total_sum = materiali_total_price + workers_price
print(total_sum)