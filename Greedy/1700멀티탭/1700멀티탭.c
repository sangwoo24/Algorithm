//
//  main.c
//  C-program
//
//  Created by 석상우 on 2020/01/13.
//  Copyright © 2020 석상우. All rights reserved.
//
#include <stdio.h>

int main()
{
	int num[101] = { 0, }, plug[101] = { 0, }, n, k, flag, id = 0, cnt = 0, lam = 0;
	int index[101] = { 0, };
	scanf_s("%d %d", &n, &k);

	for (int i = 0; i < k; i++)
		scanf_s("%d", &num[i]);

	for (int i = 0; i < k; i++)
	{
		flag = 0;
		for (int j = 0; j < n; j++)
			if (num[i] == plug[j]) flag = 1;

		if (flag) continue;

		for (int j = 0; j < n; j++)
			if (plug[j] == 0)
			{
				plug[j] = num[i];
				flag = 1;
				break;
			}

		if (flag) continue;

		// 인덱스 검사
		for (int j = 0; j < n; j++)
		{
			for (int z = i + 1; z < k; z++)
			{
				if (plug[j] == num[z])
				{
					index[id++] = z;
					break;
				}
				else cnt++;
			}
			if (cnt == (k - (i + 1)))
			{
				index[id++] = 0;
			}
		}

		int idx = 0, max = 0;
		for (int j = 0; j < n; j++)
		{
			//0일때 추가
			if (index[j] == 0)
			{
				idx = j;
				break;
			}
			else if (max < index[j])
			{
				max = index[j];
				idx = j;
			}
		}
		plug[idx] = num[i];
		lam++;
		id = 0;
	}
	printf("%d\n", lam);
	return 0;
}