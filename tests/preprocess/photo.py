def max_satisfaction(N, items):
    # 对商品进行预处理，将附件与主件关联
    main_items = []
    accessories = [[] for _ in range(len(items) + 1)]

    for i, (v, p, q) in enumerate(items):
        if q == 0:
            main_items.append((v, p, i + 1))
        else:
            accessories[q].append((v, p))

    # 初始化DP数组
    dp = [0] * (N + 1)

    # 遍历每个主件及其可能的购买组合
    for v_main, p_main, idx in main_items:
        cost_main = v_main
        satisfaction_main = v_main * p_main

        # 附件组合预处理
        combinations = [(cost_main, satisfaction_main)]  # 只购买主件

        # 单个附件和双附件组合
        for i in range(len(accessories[idx])):
            v_acc, p_acc = accessories[idx][i]
            cost_acc = v_acc
            satisfaction_acc = v_acc * p_acc

            # 添加单个附件的组合
            combinations.append((cost_main + cost_acc, satisfaction_main + satisfaction_acc))

            # 尝试与之前的每个附件组合（双附件）
            for j in range(i):
                v_acc2, p_acc2 = accessories[idx][j]
                cost_acc2 = v_acc2
                satisfaction_acc2 = v_acc2 * p_acc2

                # 添加双附件的组合
                combinations.append(
                    (cost_main + cost_acc + cost_acc2, satisfaction_main + satisfaction_acc + satisfaction_acc2))

        # 更新DP数组
        for cost, satisfaction in combinations:
            for j in range(N, cost - 1, -1):
                dp[j] = max(dp[j], dp[j - cost] + satisfaction)

    return dp[N]


# 例子
# items = [(价格, 重要度, 是否附件及所属主件编号)]
items = [
    (20, 3, 5),  # 商品1，价格20，重要度3，属于商品5
    (20, 3, 5),  # 商品2，价格20，重要度3，属于商品5
    (10, 3, 0),  # 商品3，价格10，重要度3，是主件
    (10, 2, 0),  # 商品4，价格10，重要度2，是主件
    (10, 1, 0)   # 商品5，价格10，重要度1，是主件
]
N = 50
print(max_satisfaction(N, items))
