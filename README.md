## 01. 자료형_변수

>  mutable: list, dictionary, set
>
> immutable: number, string, tuple

```python
# String (Formatting)

'Python version %d' %3
'Python version %0.2f' %3.6
'%s version' %('Python', 3)

'{lang} is easy, version {0}.{1}'.format(3, 6, lang = 'Python')
```

```python
# String (Functions)

sent = "Life is too short, You need Python"

sent.count(' ', 5, 12) 	#없으면 0 출력
sent.find(' ', 8, 12) 	#없으면 -1 출력
sent.index(' ', 8, 12)	#없으면 error 발생
sent.upper() / sent.lower()
sent.strip()
sent.replace('Python', 'Java')
sent.split(' ') 				#list로 출력
'/'.join('abcd')
```

```python
# List (Functions)

test = []

test.append('a')					#마지막 요소로 추가
test.insert(2, 'a')				#지정된 위치에 삽입
test.extend(['a', 'b']) 	#리스트 형식으로 추가해도 각각의 요소로 들어감
test.remove('a')
test.pop('a')							#마지막에 위치한 'a' 추출 후 제거
test.sort(reverse = True) #내림차순
test.reverse()						#현재 순서에서 반대로
test.index('a')
test.count('a')
```

~~~python
# Tuple (수정 및 삭제 불가능 / index 사용 가능)
~~~

```python
# Dictionary

dict_text = {(1, 2, 3) : 'tuple'} 	#수정 불가능한 요소만 key 가능
dict_list = list(dict_text.items())
del dict_list[(1, 2, 3)]
'name' in dict											#name이라는 key로 존재하는지
```

```python
# Set (중복 불가능, 순서 없음)

set('python')		#한 글자를 요소로 하는 리스트 생성
```





## 02. 제어문

```python
# If (조건부 표현식)

print('pass') if score >= 80 else print('fail')
```

```python
# While

num = 0
while num < 10:
  num += 1
  if num%2 == 0:
    continue			#num이 짝수일 때에는 넘기라는 의미
    
  print(num)
```

```python
# For (reversed)

for i in reverse(range(11)): #10부터 0까지
  print(i)
```

```python
# For (list comprehension)

result = [i*3 for i in range(10) if i%2 != 0]
```

```python
a = [1, 2, 3, 4]
result = []

for n in a:
    result.append(n*3)		#두 개가
    result += [n*3] 			#동일한 코드
print(result)
```

```python
list_a = [10, 20, 30, 40, 50, 60, 70]

for i in reversed(range(len(list_a))):
    if list_a[i] % 3 == 0:
        list_a.pop(i)		#pop은 뽑아서 추출하기 때문에 reversed로
        
print(list_a)
```





## 03. 함수





## 04. 입력_출력

