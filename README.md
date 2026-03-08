# 🧮 Python Calculator (Team Project)

Python으로 구현하는 **CLI 기반 계산기 프로그램**입니다.
이 프로젝트는 Git을 활용한 **branch 기반 협업 workflow**를 학습하기 위한 팀 프로젝트입니다.

---

# 🎯 프로젝트 목표

이 프로젝트의 목표는 다음과 같습니다.

* Python을 활용한 간단한 프로그램 구현
* Git branch 기반 협업 workflow 이해
* Pull Request 기반 협업 경험
* 팀 단위 Git 협업 경험

---

# 🛠 구현 기능

기본적으로 아래 기능을 구현해야 합니다.

```
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
```

예시 실행 결과

```
첫번째 숫자 입력: 10
연산 선택 (+ - * /): +
두번째 숫자 입력: 5

결과: 15
```

추가적으로 아래 기능을 구현할 수 있습니다.

```
- 잘못된 입력 처리
- 0으로 나누기 예외 처리
- 반복 실행 기능
```

---

# 📂 프로젝트 구조

예시 구조

```
calculator
 ┣ src
 ┃ ┗ calculator.py
 ┗ README.md
```

⚠️ **주의**

위 구조는 **예시일 뿐이며 반드시 동일하게 구현할 필요는 없습니다.**
각 팀은 **자유롭게 프로젝트 구조를 설계하여 구현해야 합니다.**

---

# 🌿 Git 협업 방식

이 프로젝트는 **Branch 기반 협업 방식**으로 진행됩니다.

각 팀은 먼저 **팀 branch를 생성**해야 합니다.

예시

```
team-1
team-2
team-3
```

이후 팀 내부에서 기능별 branch를 생성하여 개발합니다.

예시

```
feature/add
feature/subtract
feature/multiply
feature/divide
```

또는

```
team-1/add
team-1/subtract
team-1/multiply
team-1/divide
```

⚠️ **주의**

브랜치 전략은 예시이며 **반드시 동일하게 사용할 필요는 없습니다.**

각 팀은 **자체적으로 협업 전략을 설계하여 진행해야 합니다.**

---

# 🔀 권장 Git Workflow

권장되는 작업 흐름

```
1. 팀 branch 생성
2. 기능 branch 생성
3. 기능 구현
4. commit
5. GitHub push
6. Pull Request 생성
7. 팀 branch merge
```

Pull Request 기반 협업을 권장합니다.

---

# 📌 Commit 규칙

예시

```
feat: add addition function
feat: add subtraction function
fix: division by zero error
```

⚠️ **주의**

위 commit 메시지 규칙은 **예시입니다.**

각 팀은 **자체 commit 규칙을 정하여 사용해야 합니다.**

---

# ▶ 실행 방법

예시

```bash
python calculator.py
```

⚠️ 실행 방법 역시 **프로젝트 구조에 따라 달라질 수 있습니다.**

---

# 📤 제출

별도의 파일 제출은 하지 않습니다.

각 팀은 다음 정보를 제출합니다.

```
팀 branch 이름 또는 branch 링크
```

---

# ✅ 평가 기준

| 항목     | 비율  |
| ------ | --- |
| 기능 구현  | 40% |
| 코드 구조  | 10% |
| Git 사용 | 50% |

평가 시 아래 항목을 확인합니다.

* 팀 branch 존재
* 최소 **4개 이상의 branch 사용**
* Pull Request 기록 존재
* 팀 branch에 최종 코드 존재
* 프로그램 정상 실행
* README 작성

---

# ⚠️ 중요 안내

다음 사항을 반드시 확인하세요.

* 예시 코드를 그대로 복사하여 제출하는 것은 허용되지 않습니다.
* 브랜치 전략 및 프로젝트 구조는 **팀 내부에서 설계해야 합니다.**
* GitHub 협업 기록이 평가에 포함됩니다.