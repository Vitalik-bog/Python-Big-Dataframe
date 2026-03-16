 #А1 
numbers = [5, 25, 4, 5, 6, 7, 91, 10, 6]
print("Список", numbers)  

sum = 0
for num in numbers: 
 sum = sum + num

numbers.append(sum)  

print("Сумма:", sum)
print("Новый список:", numbers)


#A2
spisok = [
    ['192.168.1.4', 'Vitalik', 8, 24021],
    ['192.168.1.42', 'Boris', 4, 320],
    ['192.168.1.45', 'Vlad', 8, 10800],
    ['192.168.1.10', 'Sania', 16, 5400],
    ['192.168.1.33', 'Sergay', 2, 7200]
]

for spis in spisok:
    print(f"  IP: {spis[0]:15} | Имя: {spis[1]:10} | RAM: {spis[2]:2} Гб | Время: {spis[3]:6} сек")
#1	Подсчитать среднее время нахождения в сети (в минутах)
total_time_sec = 0
for spis in spisok:
    total_time_sec = total_time_sec + spis[3]
    
    average_time_sec = total_time_sec / len(spisok)
    average_time_min = average_time_sec / 60
    
    print(f"  Общее время всех сеансов: {total_time_sec} сек")
    print(f"  Среднее время нахождения в сети: {average_time_min:.2f} минут или в секунжах {average_time_sec:.2f}")
#2	Сформировать новый список, состоящий только из IP-адресов узлов сети

ip_addresses =[]
for spis in spisok:
    ip_addresses.append(spis[0])
print(f"  {ip_addresses}")

#	Выдать имя компьютера с наименьшим размером оперативной памяти.
min_ram = spisok[0][2]
min_ram_index = 0 # индекс компьютера с минимальной RAM

for i in range(len(spisok)):
    if spisok[i][2] < min_ram:
        min_ram = spisok[i][2]
        min_ram_index = i
        
min_ram_name = spisok[min_ram_index][1]
min_ram_value = spisok[min_ram_index][2]

print(f"  Компьютер: {min_ram_name}")
print(f"  RAM: {min_ram_value} Гб")
print(f"  IP: {spisok[min_ram_index][0]}")

#А3 Создаем словарь из 5 записей: номер заказа -> статус(Ключ- значение)
orders = {
    '101N': 'выполнен',
    '102B': 'отменен',
    '103C': 'выполнен',
    '104A': 'в обработке',
    '105D': 'выполнен'
}
for order_num, status in orders.items():
    print(f"  Заказ {order_num}: {status}")
    
    # 1. Добавляем сведения о новом заказе
print("\n Добавление нового заказа:")
orders['106E'] = 'отменен'
print(f"Добавлен заказ 106E со статусом 'отменен' ")

# Показываем обновленный словарь
print("\n  Обновленный список заказов:")
for order_num, status in orders.items():
    print(f"Заказ {order_num}: {status}")

# 2. Формируем список из номеров всех выполненных заказов
print("\n Выполненные заказы:")

completed_orders = []
for order_num in orders:
    if orders.get(order_num) == 'выполнен':
        completed_orders.append(order_num)

print(f"  Номера выполненных заказов: {completed_orders}")

# 3. Подсчитываем количество отмененных заказов
print("\n Отмененные заказы:")

cancelled_count = 0
for order_num in orders:
    if orders.get(order_num) == 'отменен':
        cancelled_count = cancelled_count + 1

print(f"  Количество отмененных заказов: {cancelled_count}")

# 4. Узнаем процент выполненных заказов
print("\nСтатистика:")

total_orders = len(orders) # Общее количество заказов
completed_count = len(completed_orders) # Количество выполненных

if total_orders > 0:
    completed_percent = (completed_count / total_orders) * 100  # Процент выполнения
    print(f"  Всего заказов: {total_orders}")
    print(f"  Выполнено: {completed_count}")
    print(f"  Отменено: {cancelled_count}")
    print(f"  Процент выполненных заказов: {completed_percent:.1f}%")
else:
    print("  Нет заказов для подсчета процента")

# Все статусы
print("\n Статусы всех заказов:")
status_list = list(orders.values())
print(f"  {status_list}")

