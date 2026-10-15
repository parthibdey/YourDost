import pandas as pd
import numpy as np

# Load data
df = pd.read_excel(r'c:\Users\parth\Downloads\Sample Data.xlsx')

# Create output file
output_file = open(r'C:\Users\parth\OneDrive\Desktop\Documents\CascadeProjects\windsurf-project\analysis_results.txt', 'w', encoding='utf-8')

def print_and_log(text):
    print(text)
    output_file.write(str(text) + '\n')

print_and_log("=" * 80)
print_and_log("SURVEY DATA ANALYSIS: PARENTS' PERCEPTIONS OF ONLINE GAMING")
print_and_log("=" * 80)

# Basic info
print_and_log(f"\nTotal Responses: {len(df)}")
print_and_log(f"Total Questions: {len(df.columns)}")

# 1. Do kids play online games?
print_and_log("\n" + "=" * 80)
print_and_log("1. ONLINE GAMING ADOPTION")
print_and_log("=" * 80)
kids_play = df['Does your kid/s play online games?'].value_counts()
print_and_log(kids_play.to_string())
print_and_log(f"\nPercentage:")
print_and_log((kids_play / len(df) * 100).to_string())

# 2. Perception statements analysis
print_and_log("\n" + "=" * 80)
print_and_log("2. PARENTAL PERCEPTIONS OF ONLINE GAMING")
print_and_log("=" * 80)

perception_cols = [col for col in df.columns if 'What would you say to the following statements regarding online gaming?' in col]
for col in perception_cols:
    print_and_log(f"\n{col.split('[')[1].rstrip(']')}:")
    print_and_log(df[col].value_counts().to_string())
    print_and_log(f"Percentages:")
    print_and_log((df[col].value_counts(normalize=True) * 100).to_string())

# 3. Fear levels analysis
print_and_log("\n" + "=" * 80)
print_and_log("3. PARENTAL FEARS ABOUT ONLINE GAMING")
print_and_log("=" * 80)

fear_cols = [col for col in df.columns if 'How much fear do you hold' in col]
for col in fear_cols:
    print_and_log(f"\n{col.split('[')[1].rstrip(']')}:")
    print_and_log(df[col].value_counts().to_string())
    print_and_log(f"Percentages:")
    print_and_log((df[col].value_counts(normalize=True) * 100).to_string())

# 4. Parental involvement
print_and_log("\n" + "=" * 80)
print_and_log("4. PARENTAL INVOLVEMENT IN GAMING")
print_and_log("=" * 80)

role_cols = [col for col in df.columns if 'Mark "True" or "False" for the following statements regarding your role in Online Gaming' in col]
for col in role_cols:
    print_and_log(f"\n{col.split('[')[1].rstrip(']')}:")
    print_and_log(df[col].value_counts().to_string())
    print_and_log(f"Percentages:")
    print_and_log((df[col].value_counts(normalize=True) * 100).to_string())

# 5. Rules in place
print_and_log("\n" + "=" * 80)
print_and_log("5. PARENTAL RULES FOR GAMING")
print_and_log("=" * 80)

rules_cols = [col for col in df.columns if 'Mark "True" or "False" for the following statements with regard to the rules' in col]
for col in rules_cols:
    print_and_log(f"\n{col.split('[')[1].rstrip(']')}:")
    print_and_log(df[col].value_counts().to_string())
    print_and_log(f"Percentages:")
    print_and_log((df[col].value_counts(normalize=True) * 100).to_string())

# 6. Impact on family
print_and_log("\n" + "=" * 80)
print_and_log("6. IMPACT ON FAMILY DYNAMICS")
print_and_log("=" * 80)

impact_cols = [col for col in df.columns if 'Mark the amount of impact' in col]
for col in impact_cols:
    print_and_log(f"\n{col.split('[')[1].rstrip(']')}:")
    print_and_log(df[col].value_counts().to_string())
    print_and_log(f"Percentages:")
    print_and_log((df[col].value_counts(normalize=True) * 100).to_string())

# 7. Demographics
print_and_log("\n" + "=" * 80)
print_and_log("7. DEMOGRAPHIC BREAKDOWN")
print_and_log("=" * 80)

print_and_log("\nKid's Age Group:")
print_and_log(df['What age group are your kid/s in?'].value_counts().to_string())
print_and_log(f"Percentages:")
print_and_log((df['What age group are your kid/s in?'].value_counts(normalize=True) * 100).to_string())

print_and_log("\nParent's Gender:")
print_and_log(df['What is your gender?'].value_counts().to_string())
print_and_log(f"Percentages:")
print_and_log((df['What is your gender?'].value_counts(normalize=True) * 100).to_string())

print_and_log("\nParent's Occupation:")
print_and_log(df['What is your occupation?'].value_counts().to_string())
print_and_log(f"Percentages:")
print_and_log((df['What is your occupation?'].value_counts(normalize=True) * 100).to_string())

# 8. Cross-tabulation: Fear vs Parental Involvement
print_and_log("\n" + "=" * 80)
print_and_log("8. CROSS-ANALYSIS: FEAR VS PARENTAL INVOLVEMENT")
print_and_log("=" * 80)

# Parents who play games vs their fear levels
played_games = df['Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I have played Online Games myself]']
fear_addiction = df['How much fear do you hold with regard to the following aspects of Online Gaming? [Online Games can be addictive]']

print_and_log("\nCross-tab: Played Games vs Fear of Addiction")
print_and_log((pd.crosstab(played_games, fear_addiction, normalize='index') * 100).to_string())

# 9. Popular games mentioned
print_and_log("\n" + "=" * 80)
print_and_log("9. POPULAR GAMES MENTIONED")
print_and_log("=" * 80)
games = df['Could you name some Online Games your kid/s play? (eg. Candy Crush, Minecraft, Call of Duty, PUBG, Counter Strike, etc.)'].dropna()
print_and_log(f"Total responses: {len(games)}")
print_and_log("\nSample of games mentioned:")
print_and_log(games.head(20).to_string())

print_and_log("\n" + "=" * 80)
print_and_log("ANALYSIS COMPLETE")
print_and_log("=" * 80)

output_file.close()
