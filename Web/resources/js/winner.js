// SETUP
  
var svg = d3.select("svg"),
    margin = { top: 20, right: 20, bottom: 30, left: 40 },
    x = d3.scaleBand().padding(0.1),
    y = d3.scaleLinear(),
    theData = undefined;

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

g.append("g")
    .attr("class", "axis axis--x");

g.append("g")
    .attr("class", "axis axis--y");


// DRAWING

function draw() {
    
    var bounds = svg.node().getBoundingClientRect(),
	width = bounds.width - margin.left - margin.right,
	height = bounds.height - margin.top - margin.bottom;
    
    x.rangeRound([0, width]);
    y.rangeRound([height, 0]);
    
    g.select(".axis--x")
	.attr("transform", "translate(0," + height + ")")
	.call(d3.axisBottom(x));
    
    //g.select(".axis--y")
    //  .call(d3.axisLeft(y).ticks(10, "%"));
    
    var bars = g.selectAll(".bar")
	.data(theData);
    
    // ENTER
    bars
	.enter().append("rect")
	.attr("class", "bar")
	.attr("x", function (d) { return x(d.user); })
	.attr("y", function (d) { return y(d.height_of_podium); })
	.attr("width", x.bandwidth())
	.attr("height", function (d) { return height - y(d.height_of_podium); });
    
    // UPDATE
    bars.attr("x", function (d) { return x(d.user); })
    //.attr("y", function (d) { return y(d.height_of_podium); })
	.attr("width", x.bandwidth())
	.attr("height", function (d) { return height - y(d.height_of_podium); });
    
    // EXIT
    bars.exit()
	.remove();
    
}

// LOADING DATA

function loadData(tsvFile) {
    
    d3.tsv(tsvFile, function (d) {
	d.height_of_podium = +d.height_of_podium;
	return d;
	
    }, function (error, data) {
	if (error) throw error;
	
	theData = data;
	
	x.domain(theData.map(function (d) { return d.user; }));
	y.domain([0, d3.max(theData, function (d) { return d.height_of_podium; })]);
	
	draw();
	
    });
}

// START!

window.addEventListener("resize", draw);
loadData("leader_board.tsb");

// ------------

// ----- Populate Contest Table --------
d3.tsv("contests.csv", function(data) {
    var table = document.getElementById("contests_table");
    var row, cell1, cell2, cell3;
    
    for (var ii = 0; ii < data.length; ii++) {
        if (ii == 0) {
	    row = table.rows[1]
	    cell1 = row.cells[0];
	    cell2 = row.cells[1];
	    cell3 = row.cells[2];
	} else {
	    row = table.insertRow(-1);
	    cell1 = row.insertCell(0);
	    cell2 = row.insertCell(1);
	    cell3 = row.insertCell(2);
	}
        cell1.innerHTML = data[ii]['Contest Name'];
	cell2.innerHTML = data[ii]['Contest Description'];
	cell3.innerHTML = data[ii]['Contest Duration'];
    }

    addRowHandlers();
    
    function addRowHandlers() {
	var table = document.getElementById("contests_table");
	var rows = table.getElementsByTagName("tr");
	for (i = 0; i < rows.length; i++) {
	    var currentRow = table.rows[i];
	    var createClickHandler =
		function(row)
	    {
		return function() {
		    var cell = row.getElementsByTagName("td")[0];
		    var id = cell.innerHTML;
		    var codeDisplayModal = document.getElementById("codeDisplayModal");
		    var codeDisplayHeader = document.getElementById("codeDisplayHeader");
		    var codeDisplay = document.getElementById("codeDisplay");
		    codeDisplayModal.style.display = "block";
		    codeDisplayHeader.innerHTML = id;
		    codeDisplay.innerHTML = "This is the code...";
		    d3.text("LikeAYoyo.py", function(data) {
			var codeDisplay = document.getElementById("codeDisplay");
			data = data.replace(/ /g, '&nbsp');
			data = data.replace(/\t/g, '&nbsp&nbsp&nbsp&nbsp');
			data = data.replace(/(?:\r\n|\r|\n)/g, '<br />');
                        codeDisplay.innerHTML = data;
		    });

		};
	    };
	    
	    currentRow.onclick = createClickHandler(currentRow);
	}
    }
});


// ----- Populate Results Table --------
d3.csv("results.csv", function(data) {
    var table = document.getElementById("results_table2");
    var row, cell1, cell2, cell3, cell4;
    
    for (var ii = 0; ii < data.length; ii++) {
        if (ii == 0) {
	    row = table.rows[1]
	    cell1 = row.cells[0];
	    cell2 = row.cells[1];
	    cell3 = row.cells[2];
	    cell4 = row.cells[3];
	} else {
	    row = table.insertRow(-1);
	    cell1 = row.insertCell(0);
	    cell2 = row.insertCell(1);
	    cell3 = row.insertCell(2);
	    cell4 = row.insertCell(3);
	}
        cell1.innerHTML = data[ii]['Contest Name'];
	cell2.innerHTML = data[ii]['Your Position'];
	var user = "Tommy";
	var temp = " Score";
	var userScoreId = user.concat(temp);
	cell3.innerHTML = data[ii][userScoreId];
	cell4.innerHTML = data[ii]['Leader Score'];
    }
});

