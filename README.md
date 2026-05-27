🚀 Full-Stack AI & Embedded Systems Portfolio
데이터 분석, 컴퓨터 비전, 딥러닝부터 회로 시뮬레이션 및 로우레벨 하드웨어 제어까지

안녕하세요! 하드웨어의 로우레벨 동작 원리를 깊이 이해하고, 이를 바탕으로 최신 AI 알고리즘을 결합해 실제 동작하는 융합 시스템을 구현하는 엔지니어 서현우입니다.

이 레포지토리는 C/ARM Cortex 기반의 시스템 프로그래밍 및 전자 회로 검증부터, Python 기반의 컴퓨터 비전, 신경망 훈련, 그리고 최신 생성형 AI 모델 연동 서비스(Lovable/Gemini)에 이르기까지 폭넓은 엔지니어링 아카이브입니다.

🛠 Tech Stacks & Core Skills
📟 Hardware & Embedded Systems
Architecture & OS: ARM Cortex 구조 이해 및 시스템 프로그래밍

Low-Level C: 동적 메모리(Stack/Heap) 최적화, 포인터 연산, MISRA C 규격을 준수하는 고신뢰성 방어적 코딩 기법 적용

Circuit Design & Verification: OrCAD Capture Lite 및 PSpice를 활용한 회로 설계, 오실로스코프 기반 실측 파형 검증 (PLL, CMOS Inverter 등)

IoT & Microcontroller: Arduino C/C++ 기반 센서(초음파, PIR 등) 데이터 수집 및 액추에이터 제어 (PWM, I2C, UART)

🧠 Data Science & AI / ML / DL
Data Analysis: NumPy(벡터화/브로드캐스팅), Pandas(전처리 파이프라인), ADsP(데이터분석준전문가) 기반의 통계적 인사이트 도출

Machine Learning: Scikit-Learn (SVM, k-NN, Linear Regression), K-Fold 교차 검증 및 하이퍼파라미터 튜닝

Deep Learning: TensorFlow & Keras 기반 다층 퍼셉트론(MLP), CNN 아키텍처 설계 및 전이 학습(Transfer Learning)

Generative AI: Gemini 2.5 API 연동, CLI/MCP(Model Context Protocol) 환경 구축, Lovable 기반 바이브 코딩(Vibe Coding)

👁️ Computer Vision
Image Processing: OpenCV 기반 공간 영역 필터링, 모폴로지(침식/팽창) 연산, 에지 검출(Canny, Sobel) 및 주파수 변환(FFT)

🌟 Highlighted Projects (핵심 프로젝트)
1. 🔬 하드웨어 회로 설계 및 로우레벨 시스템 검증
내용: 하드웨어의 전기적 특성을 분석하고, 신뢰성 높은 임베디드 시스템의 기반을 다지는 회로 시뮬레이션 및 실측 프로젝트를 수행했습니다.

기술: OrCAD PSpice, C (MISRA C), Oscilloscope

핵심 역량: 비안정 멀티바이브레이터(Astable Multivibrator) 및 CMOS 인버터 회로 설계 후 PSpice 넷리스트 에러 트러블슈팅 수행. 오실로스코프를 활용한 실제 신호 파형 측정 및 PLL 검증을 통해 시스템의 물리적 동작에 대한 이해도를 증명했습니다.

2. 🤖 생성형 AI & 로우코드 기반 웹 서비스: 'GoldenCare AI'
내용: Lovable과 Gemini CLI를 활용해 시니어 계층을 위한 음성 중심 AI 비서 앱을 기획하고, Streamlit 대시보드를 연동하여 고속 프로토타이핑(Rapid Prototyping)을 완료했습니다.

기술: Streamlit, Gemini API, Lovable, Prompt Engineering

핵심 역량: 사용자의 UI/UX를 고려한 프론트엔드/백엔드 아키텍처 기획 및 환경변수 보호 로직, API 키 핸들링을 포함한 풀스택 바이브 코딩 연동.

3. 🧠 딥러닝 기반 이미지 분류 및 비전 검출 시스템
내용: TensorFlow를 활용해 데이터를 분류하고, OpenCV를 통해 실무 환경(자동차 번호판, 하네스 케이블)의 불량을 검출하는 파이프라인을 구축했습니다.

기술: TensorFlow, OpenCV, NumPy, CNN

핵심 역량: TensorFlow 기반의 '사람 vs 말 분류기(Horse or Human)' 훈련 시 디렉토리 다운로드 및 자동화 스크립트를 구현. 모폴로지 연산과 허프 변환(Hough Transform)을 적용해 멀티 하네스 케이블의 기울기를 보정하고 노이즈를 정제하는 전처리 로직을 설계했습니다.

4. 🎮 파이썬 GUI 프로그래밍 인터랙티브 앱 구현
내용: 파이썬의 tkinter 라이브러리를 활용하여 테마 스위칭 및 애니메이션이 포함된 대화형 데스크톱 애플리케이션을 개발했습니다.

기술: Python, tkinter, OOP (객체지향 설계)

핵심 역량: '주사위 2개를 굴려 합이 7이 되는 것을 맞추는 대화형 게임' 등을 구현하며 이벤트 루프 핸들링 및 상태 관리(State Management) 능력을 학습했습니다.

📚 Detailed Learning Archive (분야별 상세 학습 노트)
메모리 최적화: 동적 할당(malloc/free) 시 발생할 수 있는 메모리 누수 방지 및 포인터 연산의 안전성 확보

제어 흐름 및 표준 준수: 시스템 오작동을 막기 위한 MISRA C 규격 기반의 엄격한 변수 캐스팅 및 제어문 설계

파이썬 코어: 추상화, 다형성 등 객체지향 원리 이해 및 제너레이터를 활용한 대용량 데이터 메모리 효율적 처리

NumPy & Pandas: 올림차순(Ascending) 정렬, 조건부 데이터 파싱(.loc), 결측치 처리 및 C언어 기반 연속 메모리 할당(NumPy)의 속도 이점 검증

신경망 모델링: Adam, RMSprop 등 옵티마이저 특성 비교 및 ImageDataGenerator를 통한 과적합 방지, 조기 종료(Early Stopping) 셋업

기하학 및 변환: 어파인(Affine), 원근 투시(Perspective) 변환을 통한 3차원 공간 투영 및 객체 분할(Segmentation)

📩 Contact: [nuclear4569@naver.com]
