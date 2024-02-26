import numpy as np
import random
from read import read_dist,scenic_dict
# 假设 graph 是一个邻接矩阵，表示图的连接情况
# 这里只是一个示例，实际情况需要根据具体图的类型来定义
graph1=np.array(read_dist(1))


# 遗传算法的参数
POP_SIZE = 50
ITERATIONS = 1000
P_CROSSOVER = 0.7  # 交叉概率
P_MUTATION = 0.1   # 变异概率

# 生成初始种群
def generate_population(size, vertices):
    population = []
    for _ in range(size):
        individual = random.sample(vertices, len(vertices))
        population.append(individual)
    return population

# 计算个体的适应度
def fitness_function(individual, graph):
    fitness = 0
    for i in range(len(individual) - 1):
        fitness += graph[individual[i]][individual[i + 1]]
    return fitness

# 选择操作
def selection(population):
    population = sorted(population, key=lambda x: fitness_function(x, graph1), reverse=True)
    return population[:2]

# 交叉操作
def crossover(parent1, parent2):
    size = len(parent1)
    crossover_point = random.randint(1, size - 1)
    child = parent1[:crossover_point] + [x for x in parent2 if x not in parent1[:crossover_point]]
    return child

# 变异操作
def mutation(individual):
    index1, index2 = random.sample(range(len(individual)), 2)
    individual[index1], individual[index2] = individual[index2], individual[index1]

# 主函数
def main():
    vertices = range(len(graph1))
    population = generate_population(POP_SIZE, vertices)

    for _ in range(ITERATIONS):
        population = selection(population)
        child = crossover(population[0], population[1])
        mutation(child)
        population.append(child)
        population = population[-POP_SIZE:]

    best_path = population[0]
    print('推荐路径：')
    day1=best_path[0:4]
    day2=best_path[4:8]
    day3=best_path[8:]
    day=[day1,day2,day3]
    for i in range(3):
        print(f"第{i+1}天:")
        for j in day[i]:
            if j!=day[i][-1]:
                print(scenic_dict[j],'-->',end='')
            else:
                print(scenic_dict[j])
        print("")

if __name__ == "__main__":
    main()
