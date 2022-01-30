

difference(){
	union(){

        translate([15,0,0]){
            cube([250-17,3,8], center=false);
        }         
        translate([15,-4,0]){
            cube([3,11,8], center=false);
        }         

        translate([0,-4,0]){
            cube([15,3,8], center=false);
        }         
        translate([0,4,0]){
            cube([15,3,8], center=false);
        }         

	}
	union() {
        translate([3,5,4]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         
        translate([3+240,5,4]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         

        
	}
}
