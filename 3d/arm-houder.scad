

difference(){
	union(){

        translate([12,-14,0]){
            cube([3,31,8], center=false);
        }         

        translate([0,-4.5,0]){
            cube([15,3,8], center=false);
        }         
        translate([0,4.5,0]){
            cube([15,3,8], center=false);
        }         

	}
	union() {
        translate([3,8,4]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.2, $fn=100, center=false);
            }
        }         
        translate([0,1.5-12,4]){
            rotate([0,90,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         
        translate([0,1.5+12,4]){
            rotate([0,90,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         

        
	}
}
