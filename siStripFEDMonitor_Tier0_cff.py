import FWCore.ParameterSet.Config as cms

from DQM.SiStripMonitorHardware.siStripFEDMonitor_cfi import *

#disable error output: enabled in P5 configuration for errors.
siStripFEDMonitor.PrintDebugMessages = 0
#lumi histogram
siStripFEDMonitor.ErrorFractionByLumiBlockHistogramConfig.Enabled = True
#Global/summary histograms
siStripFEDMonitor.FedEventSizeHistogramConfig.Enabled = False
siStripFEDMonitor.DataPresentHistogramConfig.Enabled = True
siStripFEDMonitor.AnyFEDErrorsHistogramConfig.Enabled = True
siStripFEDMonitor.AnyDAQProblemsHistogramConfig.Enabled = True
siStripFEDMonitor.AnyFEProblemsHistogramConfig.Enabled = True
siStripFEDMonitor.CorruptBuffersHistogramConfig.Enabled = True
siStripFEDMonitor.BadChannelStatusBitsHistogramConfig.Enabled = True
siStripFEDMonitor.BadActiveChannelStatusBitsHistogramConfig.Enabled = True
#sub sets of FE problems
#siStripFEDMonitor.FEOverflowsHistogramConfig.Enabled = False
#siStripFEDMonitor.FEMissingHistogramConfig.Enabled = False
#siStripFEDMonitor.BadMajorityAddressesHistogramConfig.Enabled = False
siStripFEDMonitor.BadMajorityInPartitionHistogramConfig.Enabled = False
siStripFEDMonitor.FeMajFracTIBHistogramConfig.Enabled = False
siStripFEDMonitor.FeMajFracTOBHistogramConfig.Enabled = False
siStripFEDMonitor.FeMajFracTECBHistogramConfig.Enabled = False
siStripFEDMonitor.FeMajFracTECFHistogramConfig.Enabled = False
#Sub sets of DAQ problems
siStripFEDMonitor.DataMissingHistogramConfig.Enabled = False
siStripFEDMonitor.BadIDsHistogramConfig.Enabled = False
siStripFEDMonitor.BadDAQPacketHistogramConfig.Enabled = False
siStripFEDMonitor.InvalidBuffersHistogramConfig.Enabled = False
siStripFEDMonitor.BadDAQCRCsHistogramConfig.Enabled = False
siStripFEDMonitor.BadFEDCRCsHistogramConfig.Enabled = False
#TkHistoMap
siStripFEDMonitor.TkHistoMapHistogramConfig.Enabled = True
#Detailed FED level expert histograms
siStripFEDMonitor.FEOverflowsDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.FEMissingDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.BadMajorityAddressesDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.BadAPVStatusBitsDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.APVErrorBitsDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.APVAddressErrorBitsDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.UnlockedBitsDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.OOSBitsDetailedHistogramConfig.Enabled = False
siStripFEDMonitor.FETimeDiffTIBHistogramConfig.Enabled = True
siStripFEDMonitor.FETimeDiffTOBHistogramConfig.Enabled = True
siStripFEDMonitor.FETimeDiffTECBHistogramConfig.Enabled = True
siStripFEDMonitor.FETimeDiffTECFHistogramConfig.Enabled = True
siStripFEDMonitor.ApveAddressHistogramConfig.Enabled = True
siStripFEDMonitor.FeMajAddressHistogramConfig.Enabled = True
#medians per APV for all channels, all events
siStripFEDMonitor.MedianAPV0HistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  NBins = cms.untracked.uint32(256),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(1024)
  )
siStripFEDMonitor.MedianAPV1HistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  NBins = cms.untracked.uint32(256),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(1024)
  )
#Error counting histograms
siStripFEDMonitor.nFEDErrorsHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(441),
  Min = cms.untracked.double(-0.5),
  Max = cms.untracked.double(440.5)
)
#siStripFEDMonitor.nFEDDAQProblemsHistogramConfig = cms.untracked.PSet(
#  Enabled = cms.untracked.bool(True),
#  NBins = cms.untracked.uint32(101),
#  Min = cms.untracked.double(-0.5),
#  Max = cms.untracked.double(100.5)
#)
#siStripFEDMonitor.nFEDsWithFEProblemsHistogramConfig = cms.untracked.PSet(
#  Enabled = cms.untracked.bool(True),
#  NBins = cms.untracked.uint32(101),
#  Min = cms.untracked.double(-0.5),
#  Max = cms.untracked.double(100.5)
#)
#siStripFEDMonitor.nFEDCorruptBuffersHistogramConfig = cms.untracked.PSet(
#  Enabled = cms.untracked.bool(True),
#  NBins = cms.untracked.uint32(101),
#  Min = cms.untracked.double(-0.5),
#  Max = cms.untracked.double(100.5)
#)
#bins size number of FE Units/10, max is n channels
siStripFEDMonitor.nBadChannelStatusBitsHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nBadActiveChannelStatusBitsHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
#siStripFEDMonitor.nFEDsWithFEOverflowsHistogramConfig = cms.untracked.PSet(
#  Enabled = cms.untracked.bool(False),
#  #NBins = cms.untracked.uint32(101),
#  #Min = cms.untracked.double(-0.5),
#  #Max = cms.untracked.double(100.5)
#)
#siStripFEDMonitor.nFEDsWithMissingFEsHistogramConfig = cms.untracked.PSet(
#  Enabled = cms.untracked.bool(False),
#  #NBins = cms.untracked.uint32(101),
#  #Min = cms.untracked.double(-0.5),
#  #Max = cms.untracked.double(100.5)
#)
#siStripFEDMonitor.nFEDsWithFEBadMajorityAddressesHistogramConfig = cms.untracked.PSet(
#  Enabled = cms.untracked.bool(False),
#  #NBins = cms.untracked.uint32(101),
#  #Min = cms.untracked.double(-0.5),
#  #Max = cms.untracked.double(100.5)
#)
siStripFEDMonitor.nUnconnectedChannelsHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(6000),
  Max = cms.untracked.double(8000)
)
siStripFEDMonitor.nAPVStatusBitHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(250),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(500)
)
siStripFEDMonitor.nAPVErrorHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nAPVAddressErrorHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nUnlockedHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nOutOfSyncHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nTotalBadChannelsHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nTotalBadActiveChannelsHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(250),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(500)
)
siStripFEDMonitor.nTotalBadChannelsvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  NBins = cms.untracked.uint32(600),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nTotalBadChannelsvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(2400),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(150)
)
siStripFEDMonitor.nTotalBadActiveChannelsvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  NBins = cms.untracked.uint32(600),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nTotalBadActiveChannelsvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
  NBins = cms.untracked.uint32(2400),
  Min = cms.untracked.double(0),
  Max = cms.untracked.double(150)
)
siStripFEDMonitor.nFEDErrorsvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nFEDErrorsvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
)
siStripFEDMonitor.nFEDCorruptBuffersvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nFEDCorruptBuffersvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
)
siStripFEDMonitor.nFEDsWithFEProblemsvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nFEDsWithFEProblemsvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
)
siStripFEDMonitor.nAPVStatusBitvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nAPVStatusBitvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
)
siStripFEDMonitor.nAPVErrorvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nAPVErrorvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
)
siStripFEDMonitor.nAPVAddressErrorvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nAPVAddressErrorvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
)
siStripFEDMonitor.nUnlockedvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nUnlockedvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
)
siStripFEDMonitor.nOutOfSyncvsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.nOutOfSyncvsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(True),
)
siStripFEDMonitor.FedMaxEventSizevsTimeHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
  #NBins = cms.untracked.uint32(600),
  #Min = cms.untracked.double(0),
  #Max = cms.untracked.double(3600)
)
siStripFEDMonitor.FedMaxEventSizevsLumisectionHistogramConfig = cms.untracked.PSet(
  Enabled = cms.untracked.bool(False),
)
siStripFEDMonitor.FedIdVsApvIdHistogramConfig = cms.untracked.PSet(
    Enabled = cms.untracked.bool(True)
)
        
