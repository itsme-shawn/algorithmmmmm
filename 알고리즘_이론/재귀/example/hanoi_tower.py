def move_disk(disk_num, start_peg, end_peg):
  print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
  # base case : 옮길 원판이 없으면 함수를 끝낸다.
  if(num_disks == 0):
    return
  other_pug = 6 - (start_peg + end_peg)

  # 가장 큰 원판을 제외하고 나머지 원판들을 start 에서 other로 이동
  hanoi(num_disks-1, start_peg, other_pug)

  # 가장 큰 원판을 start 에서 end 로 이동
  move_disk(num_disks, start_peg, end_peg)

  # 나머지 원판들은 other 에서 end 로 이동
  hanoi(num_disks-1, other_pug, end_peg)

hanoi(3, 1, 3)

# 시간복잡도 : hanoi 함수는 계속해서 부분문제 2개를 만들어낸다. 재귀적인 부분을 제외하면 hanoi 함수의 시간복잡도는 O(1) 이므로 총 시간복잡도는 O(2^n) 이 된다.

# 하노이의 탑 내부 로직이 잘 이해가 안된가면 나뭇가지 형식으로 재귀함수호출되는 형태를 그려보자.