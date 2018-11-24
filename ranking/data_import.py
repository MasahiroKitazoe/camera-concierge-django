import pandas as pd
import math
import numpy as np


def assign_item(item):
    if type(item) == float and math.isnan(item):
      return 0
    else:
      if type(item) == str:
        item = item.replace("\u3000", " ")
      return item


def import_csv_into_model(file_path, target_model):
    df = pd.read_csv(file_path, encoding='utf-8')
    fields = target_model._meta.get_fields()
    for _, row in df.iterrows():
      data_dict = {}
      for i, field in enumerate(fields):
        if field.get_internal_type() == "IntegerField":
          data_dict[field.name] = int(assign_item(row[i]))
        elif field.get_internal_type() == "FloatField":
          data_dict[field.name] = float(assign_item(row[i]))
        else:
          data_dict[field.name] = assign_item(row[i])
      instance = target_model(**data_dict)
      instance.save()
