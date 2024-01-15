import pandas as pd 
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt

data = pd.read_csv("Data Extraction Responses.csv")

data["Year Published"] = data["Year Published"].astype(int)

permModels = data[(data['Trained on file level code'] == 'Yes') & (data['Reference to Permissive code'] == 'Yes')]

unpermModels = data[(data['Trained on file level code'] == 'Yes') & (data['Reference to Permissive code'] == 'No')]

modelsOnFileCode = data[(data['Trained on file level code'] == 'Yes')]

modelsOnCode = data[(data['Trained on code'] == 'Yes')]

# Mentioned they are permissive
permWork = permModels.groupby('Year Published')['Reference to Permissive code'].count().reset_index(name='PermRef')

# Not specifically mentioned if permissive (does not mean they are not permissive)
unpermWork = unpermModels.groupby('Year Published')['Reference to Permissive code'].count().reset_index(name='NoPermRef')

trainedOnCode = modelsOnCode.groupby('Year Published')["Trained on code"].count().reset_index()


permWork["PermRef"] = (permWork["PermRef"] / len(modelsOnFileCode)).round(2)

unpermWork["NoPermRef"] = (unpermWork["NoPermRef"] / len(modelsOnFileCode)).round(2)

trainedOnCode["Trained on code"] = (trainedOnCode["Trained on code"] / len(modelsOnCode)).round(2)



sns.set_style('darkgrid')
sns.barplot(x = "Year Published", y = "PermRef", data = permWork)
plt.xlabel('Year Published', fontweight='bold')
plt.ylabel('Permissive Codebase Percentage', fontweight='bold')
plt.title('Annual Distribution of LLMs Trained on Permissive File Code', fontweight='bold')
plt.savefig('permissive_code.png', dpi=250)
plt.clf()

sns.barplot(x = "Year Published", y = "Trained on code", data = trainedOnCode)
plt.xlabel('Year Published', fontweight='bold')
plt.ylabel('Trained on Code Percentage', fontweight='bold')
plt.title('Annual Distribution of LLMs Trained on Any Code', fontweight='bold')
plt.savefig('trained_code.png', dpi=250)

# plt.show()


