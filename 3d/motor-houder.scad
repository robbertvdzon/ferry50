

difference(){
	union(){

        translate([0,0,0]){
            cube([55,3,23], center=false);
        }         
        translate([-10,0,0]){
            cube([75,14,3], center=false);
        }         



	}
	union() {

        translate([(55-41)/2,-1,3]){
            cube([41,5,23], center=false);
        }         

        translate([55/2-33,10,-1]){
            rotate([0,0,0]){
                cylinder(h=117, r=2, $fn=100, center=false);
            }
        }         
        translate([55/2+33,10,-1]){
            rotate([0,0,0]){
                cylinder(h=117, r=2, $fn=100, center=false);
            }
        }         
        
        translate([55/2-48/2,20,18]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.8, $fn=100, center=false);
            }
        }         
        translate([55/2+48/2,20,18]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.8, $fn=100, center=false);
            }
        }         
        
	}
}
