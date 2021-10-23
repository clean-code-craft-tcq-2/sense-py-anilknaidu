import unittest
import statistics
import math

############################# StatsTest ####################################
#Below class is used to unit test the ComputeStats functionality from Module
#statistics.

#Testcase1: Check if Min, max and average values are almost in range +/-
#delta epsilon

#Testcase2: Incase Average/max/Min are Nans, check if the same is returned by
#functionality

#Testcase3: Check if Email and LED alerts are sent in case the Max value
#exceeds the threshold mentioned.
############################################################################


class StatsTest(unittest.TestCase):                                       #Check if calculated average, Max and Min are in range of +/- delta of known values
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)
  
  def test_avg_is_nan_for_empty_input(self):                              #Check if nan is returned by the calculateStats functionality in case of NaN input
    computedStats = statistics.calculateStats([math.nan,0,-1])
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html
    self.assertEqual(math.isnan(computedStats["avg"]), True)
    self.assertEqual(math.isnan(computedStats["max"]), True)
    self.assertEqual(math.isnan(computedStats["min"]), True)

  def test_raise_alerts_when_max_above_threshold(self):                   #Check if alerts are sent in case the Max value in List exceeds the threshold mentioned.
    emailAlert = statistics.EmailAlert()
    ledAlert = statistics.LEDAlert()
    maxThreshold = 10.5                                                   #Threshold
    statsAlerter = statistics.StatsAlerter(maxThreshold, [emailAlert.sendEmail(), ledAlert.alert()])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent())
    self.assertTrue(ledAlert.ledGlows())
    
      
if __name__ == "__main__":
  unittest.main()
    
