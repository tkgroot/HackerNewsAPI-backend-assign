// Chart Generation

// Define Bar colors
const orange = {
  backgroundColor: "rgb(255, 118, 13)",
  borderColor: "rgb(255, 118, 13)"
};
const gold = {
  backgroundColor: "rgb(255, 174, 0)",
  borderColor: "rgb(255, 174, 0)"
};
const yellow = {
  backgroundColor: "rgb(255, 227, 13)",
  borderColor: "rgb(255, 227, 13)"
};

// Store the most frequent words
// let wordList = []; // ["Words", "May", "Never", "Be", "The", "Same"];

const barChartData = {
  labels: [],
  datasets: []
};

const barChartOptions = {
  // Elements options apply to all of the options unless overridden in a dataset
  // In this case, we are setting the border of each horizontal bar to be 2px wide
  elements: {
    rectangle: {
      borderWidth: 2
    }
  },
  responsive: true,
  legend: {
    position: "right"
  },
  tooltips: {
    enabled: true
  },
  title: {
    display: false
  }
};

//
// Create Chart
//
window.onload = function() {
  const ctx = document.getElementById("horizontalBarChart").getContext("2d");
  window.barChart = new Chart(ctx, {
    type: "horizontalBar",
    data: barChartData,
    options: barChartOptions
  });
};

//
// Update Chart
//
window.setInterval(() => {
  window.barChart.update();
}, 5000);

// API Query Helper
const query = (label, color, url, btnID) => {
  $(() => {
    const newDataset = {
      label: label,
      data: [],
      ...color
    };

    $.getJSON(url, data => {
      $("#" + btnID).html(JSON.stringify(data)); // update code field

      labels = barChartData.labels;
      dataset = barChartData.datasets;
      new_labels = [];
      new_data = [];

      for (idx in data) {
        let [label, value] = data[idx];

        if (barChartData.labels.length === 0) {
          new_labels.push(label);
          new_data.push(value);
        } else {
          label_idx = barChartData.labels.findIndex(elm => elm === label);

          if (label_idx < 0) {
            barChartData.labels.push(label);
            console.log(barChartData.labels.length);
            for (let i = 0; i < barChartData.labels.length; i++) {
              if (!new_data[i] > 0) {
                new_data[i] = 0;
              }
            }
            new_data[barChartData.labels.length - 1] = value;
          } else {
            for (let i = 0; i < label_idx; i++) {
              if (!new_data[i] > 0) {
                new_data[i] = 0;
              }
            }
            new_data[label_idx] = value;
          }
        }
      }

      if (new_labels.length > 0) {
        new_labels.forEach(elm => {
          barChartData.labels.push(elm);
        });
      }
      new_data.forEach(elm => {
        newDataset.data.push(elm);
      });
      // Add newDataset
      barChartData.datasets.push(newDataset);
      barChartData.labels.concat([]);
    });
  });
};

// Query API Endpoint Task 1
document.getElementById("APIEndpoint1").addEventListener("click", function() {
  query(
    (label = "Query1"),
    (color = orange),
    (url = "api/twenty_five_stories"),
    (btnID = "lateststories")
  );
});

// Query API Endpoint Task 2
document.getElementById("APIEndpoint2").addEventListener("click", function() {
  query(
    (label = "Query2"),
    (color = gold),
    (url = "api/days_of_posts"),
    (btnID = "daysofposts")
  );
});

// Query API Endpoint Task 3
document.getElementById("APIEndpoint3").addEventListener("click", function() {
  query(
    (label = "Query3"),
    (color = yellow),
    (url = "api/karma_stories"),
    (btnID = "karmastories")
  );
});
