# 81 85

import pandas

csv = pandas.read_excel("Copy of Online Awareness and Security Form (Responses).xlsx")


# cleaning bad/empty values:
#
# for curr_column in range(81, 86):
#     cname = csv.columns[curr_column]
#     csv = csv[csv[cname].astype(str).str.strip().str.len() >= 3]

needed_subsection = csv.iloc[:, 81:86]

needed_subsection.to_excel("cleaned_data.xlsx", index=False)

