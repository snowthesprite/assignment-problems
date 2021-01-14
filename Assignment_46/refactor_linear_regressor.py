    def calculate_coefficient(self):
        finished_coeff = {}
        print(list(self.df.data_dict.values()))
        mat = [[1 for x in list(self.df.data_dict.values())[0]]]
        independ_vars = {}
        for key in self.df.data_dict:
          if key != self.dependent_variable:
            independ_vars[key] = self.df.data_dict[key]
        for row in range(len(independ_vars)):
          mat.append(list(self.df.data_dict.values())[row][0])
        print(mat)
        mat = Matrix(mat)
        print(mat.elements)
        mat = mat.transpose()
        mat_t = mat.transpose()
        mat_mult = mat_t.matrix_multiply(mat)
        mat_inv = mat_mult.inverse()
        mat_pseudoinv = mat_inv.matrix_multiply(mat_t)
        multiplier = [[num] for num in list(self.df.data_dict.values())[1][0]]
        multiplier_mat = mat_pseudoinv.matrix_multiply(Matrix(multiplier))
        for num in range(len(multiplier_mat.elements)):
          if num == 0:
            key = 'constant'
          else:
            key = list(self.df.data_dict.keys())[num-1]
          finished_coeff[key] = [row[0] for row in multiplier_mat.elements][num]
        return finished_coeff