import streamlit as st

st.set_page_config(page_title="과일 가격 계산기", page_icon="🍎")

st.title("🍓 과일 가격 계산기")

# 기본 가격 입력
value = st.number_input("과일의 기본 가격을 입력하세요", min_value=1, step=1)

# 성장 변이 선택
growth_mutation = st.radio("성장 변이를 선택하세요", ["일반", "골드", "레인보우"])
growth_mutation_multiples = {"일반": 1, "골드": 20, "레인보우": 50}[growth_mutation]

# 돌연변이 목록
mutation_data = [
    ("wet", "웻", 1),
    ("Chilled", "칠드", 1),
    ("Frozen", "프로즌", 9),
    ("Shocked", "쇼크드", 99),
    ("Moonlit", "문라이트", 1),
    ("Choc", "초코", 1),
    ("Disco", "디스코", 124),
    ("Bloodlit", "블러드라이트", 3),
    ("Celestial", "셀레스티얼", 119),
    ("Zombified", "좀비", 24),
    ("Plasma", "플라즈마", 4),
    ("Voidtouched", "보이드터치", 134),
    ("pollinated", "수분받음", 2),
    ("HoneyGlazed", "허니글레이즈", 4),
    ("Heavenly", "헤븐리", 4),
    ("Dawnbound", "던바운드", 149),
    ("Molten", "몰튼", 24),
    ("Meteoric", "메테오릭", 124),
    ("Burnt", "번트", 3),
]

st.markdown("### ✅ 붙어있는 돌연변이를 선택하세요")
selected_mutations = []
Weather_Mutation = 1

for eng, kor, bonus in mutation_data:
    checked = st.checkbox(f"{kor} ({eng}) : +{bonus}")
    if checked:
        selected_mutations.append((kor, eng, bonus))
        Weather_Mutation += bonus

# 계산 버튼
if st.button("💰 가격 계산하기"):
    final_price = value * growth_mutation_multiples * Weather_Mutation

    st.markdown("---")
    st.subheader("📦 계산 결과")
    st.write(f"기본 가격: **{value:,} 원**")
    st.write(f"성장 변이 배수: **{growth_mutation_multiples}배**")
    st.write(f"돌연변이 총 배수: **{Weather_Mutation}배**")

    # 선택된 돌연변이 보여주기
    if selected_mutations:
        st.markdown("**적용된 돌연변이:**")
        for kor, eng, bonus in selected_mutations:
            st.write(f"- {kor} ({eng}) +{bonus}")
    else:
        st.write("적용된 돌연변이가 없습니다.")

    st.markdown(f"### 💰 최종 가격: **{final_price:,} 원**")
