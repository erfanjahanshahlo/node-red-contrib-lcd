module.exports = function(RED) {
    var exec = require("child_process").exec;
    function LiquidCrystal(config) {
        RED.nodes.createNode(this, config);
	this.pinstype = config.pinstype;
        var node = this;
        this.on("input", function(msg) {
	    if (node.pinstype) {
		text = msg.payload.replace(" ", "#/@$%");
	        exec('python2 "' + __dirname + '/lcd.py" ' + node.pinstype + " " + text, function(err, stdout, stderr) {
  		    if (err) {
    		        node.error(err, msg); 
		        node.status({fill: "red", shape: "dot", text: "ERROR"});
  		    } else {
			node.status({fill: "green", shape: "dot", text: "OK"});
		    }
	        });
	    } else {
		node.error("Please set lcd pins and rows & cols", msg); 
	    }
        });
        this.on("close", function() {
        });
    }
    RED.nodes.registerType("lcd", LiquidCrystal);
}