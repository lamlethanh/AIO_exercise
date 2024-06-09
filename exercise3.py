import math
import random


def MAE(y1, y2):
    return abs(y1 - y2)

def MSE(y1, y2):
    return pow(y1-y2, 2)

def RMSE(y1,y2):
    return math.sqrt(MSE(y1, y2))

def cal_loss(y1, y2, name):
    if (name == "MAE"):
        return MAE(y1, y2)
    elif (name == "RMSE"):
        return RMSE(y1, y2)
    else:
        return MSE(y1, y2)
    return result

def choose_regress_loss_func():
    num_sample = input("Input number of samples (integer number) which are generated: ")
    if (num_sample.isnumeric()):
        num_sample = int(num_sample)
        loss_name = input("Input loss name (MAE | MSE | RMSE): ")
        if (loss_name == "MAE" or loss_name == "RMSE" or loss_name == "MSE"):
            loss_arr = []
            for i in range(0, num_sample):
                pred_temp = random.uniform(0,10)
                target_temp = random.uniform(0,10)
                loss_temp = cal_loss(target_temp, pred_temp, loss_name)
                print(f"loss name: {loss_name}, sample: {i}, pred: {pred_temp}, target: {target_temp} ,")
                print(f"\t loss: {loss_temp}")
                loss_arr.append(loss_temp)
            final_loss = sum(loss_arr)/num_sample
            if (loss_name == "RMSE"):
                final_loss = math.sqrt(final_loss)
            print(f"final {loss_name}: {final_loss}")
        else:
            print(f"{loss_name} is not supported")

choose_regress_loss_func()
            