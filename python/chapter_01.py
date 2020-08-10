# Chapter 02-1
# 파이썬 완전기초
# Print 사용법

#테스트
# 기본출력
print('Python start!')
print("Python start!")
print('''Python start!''')
print("""Python start!""")


# separator 옵션
print('p','b','b','c',sep='')
print('010','6666','4567',sep='-')


# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()


# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()


# format 사용(d  : 3 , s  : 'python', f : 3.14454544)
print('%s %s' % ('one','two'))
print('{} {}' .format('one','two'))
print('{1} {0}' .format('one','two'))

print()

# %{value for value in variable}
print('%10s' %('nice'))
print('{:>10}' .format('nice'))

print('%-10s' %('nice'))
print('{:10}' .format('nice'))

print('{:$>10}' .format('nice'))
print('{:$^10}' .format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudynice'))
print('%5s' % ('pythonstudynice'))
print('{:10.5}' .format('pythonstudynicd'))

# %{key: value for key, value in variable}
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42))

print()

# %f

print('%f' % (3.1434434324))
print('%1.4f' % (3.1434434324))

print('{:f}' .format(3.1434434324))

print('%06.2f' % (3.1434434324))
print('{:06.2f}' .format(3.1434434324))

print()
