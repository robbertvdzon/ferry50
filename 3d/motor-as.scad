

difference(){
	union(){

        translate([0,0,0]){
            cube([210,3,8], center=false);
        }         

	}
	union() {
        translate([3,5,4]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         
        translate([3+27,5,4]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         
        translate([3+200,5,4]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         

        
	}
}
