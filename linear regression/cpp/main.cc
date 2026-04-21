// imports ------------------------------------------------
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <ios>
// definition ---------------------------------------------
#define scalar double
#define feature std::vector<scalar>
#define matrix std::vector<feature>
#define model std::pair<double, double>  // <w, b>

// Function declaration -----------------------------------
double mean_square_error(double y, double yh);
double mean_absolute_error(double y, double yh);
double root_mean_square_error(double y, double yh);

matrix load_csv(const std::string& path);

scalar predict(model);
model learn(matrix& dataset, double epoch);
model update_weight_bias(matrix dataset, double weight, double bias, double learning_rate);

// Function definition ------------------------------------
double mean_square_error(const double y, const double yh) {
    return (y - yh) * (y - yh);
}

scalar predict(const model& trained_model, const double input) {
    // m = trained_model.first
    // c = trained_model.second
    return trained_model.first * input + trained_model.second;
}

matrix load_csv(const std::string& path) {
    std::fstream file;
    std::cout << "Loading file : " << path << std::endl;
    try {
        file.open(path, std::ios::in);
    } catch (int e) {
        std::cerr << "Failed to open the file : " << path << std::endl;
    }
    std::string temp, line, word;
    feature row;
    matrix dataset;
    unsigned int total_rows = 0;

    while (file) {
        row.clear();
        getline(file, line);
        std::stringstream s(line);

        while (getline(s, word, ',')) {
            row.push_back(std::stod(word));
        }
        dataset.push_back(row);
        total_rows++;
    }
    std::cout << "Total rows : " << total_rows << std::endl;
    return dataset;
}

model learn(const matrix& dataset, const unsigned int epochs) {
    double w = 1, b = 1;
    double lr = 0.00000001;
    const unsigned int count = dataset.size();

    for (int epoch = 0; epoch < epochs; epoch++) {

        double dw = 0, db = 0;
        double total_loss = 0;

        for (const auto& each : dataset) {
            double x = each[0];
            double y = each[1];

            double yh = w * x + b;
            double error = mean_square_error(y, yh);

            dw += -2 * x * error;
            db += -2 * error;

            total_loss += error * error;
        }
        
        // Gradient Descent
        dw /= count;
        db /= count;

        // Descending the w and b based on the derived cost
        w -= lr * dw;
        b -= lr * db;

        double loss = total_loss / count;

        if (epoch % 100 == 0) {
            std::cout << "Epoch: " << epoch
                      << " Loss: " << loss
                      << " w: " << w
                      << " b: " << b << std::endl;
        }
    }

    return {w, b};
}

// Main execution
int main() {
    std::cout << "Linear Regression Execution" << std::endl;
    const matrix dataset = load_csv("/home/vivekofficemachine01/CLionProjects/linreg/dataset.csv");
    const model trained_model = learn(dataset, 10000000000);
    std::cout << "Predicted Value for 800 : Rs." << predict(trained_model, 800) << std::endl;
    return 0;
}




