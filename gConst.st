{attribute 'qualified_only'}
VAR_GLOBAL CONSTANT
	/// REAL NULL Sentinel
	gc_rlNULL : REAL := -3.402823E+38;
	/// REAL SQL MAX Value
	gc_rlMAX : REAL := 1.0E+38;
	/// REAL SQL MIN Value
	gc_rlMIN : REAL := -1.0E+38;
	/// DT NULL Sentinel
	gc_dtNULL : DT := DT#1970-1-1-0:0:0;
	gc_rlLongStr : REAL := 123456789.123456789;
	gc_iMax : INT := 32767;
	gc_iMin : INT := -32768;
	gc_diMax : DINT := 2147483647;
	gc_diMin : DINT := -2147483648;
	gc_tMax : TIME := T#49D17H2M47S295MS;
	gc_dtLongest : DT := DT#2105-12-11-16:28:15;
	gc_sLorem : STRING(255) := 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi rutrum ante a luctus gravida. Sed tincidunt volutpat luctus. Maecenas molestie ex velit, in dignissim libero rutrum bibendum. Aenean ac urna rhoncus, lobortis orci non, venenatis libero fusce.';
	gc_sDisable : STRING(10) := 'disabled_';

END_VAR
