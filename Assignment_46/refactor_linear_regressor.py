def calculate_coefficient(self):
    finished_coeff = {}
    data_dict_data = list(self.df.data_dict.values())
    line_eqn = [[1 for _ in data_dict_data[0]]]
    independent_variable = {}
    for key in self.df.data_dict:
        if key != self.dependent_variable:
            independent_variable[key] = self.df.data_dict[key]
    for row in range(len(independent_variable)):
        line_eqn.append(data_dict_data[row][0])
    line_eqn = Matrix(line_eqn)
    line_eqn_t = line_eqn.transpose()
    line_eqn_mult = line_eqn_t.matrix_multiply(line_eqn)
    line_eqn_inv = line_eqn_mult.inverse()
    line_eqn_pseudoinv = line_eqn_inv.matrix_multiply(line_eqn_t)
    multiplier = [data_dict_data[1][0]]
    multiplier_x_pseudoinv = line_eqn_pseudoinv.matrix_multiply(Matrix(multiplier)).elements
    finished_coeff['constant'] = multiplier_x_pseudoinv[0][0] #that should be the right idex
    for num in range(len(multiplier_x_pseudoinv)):
        key = list(self.df.data_dict)[num-1]
        finished_coeff[key] = [row[0] for row in multiplier_x_pseudoinv][num]
    return finished_coeff
