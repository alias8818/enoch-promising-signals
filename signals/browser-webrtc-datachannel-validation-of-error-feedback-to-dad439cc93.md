# Browser WebRTC Datachannel Validation of Error-Feedback Top-K Gossip

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `browser-webrtc-datachannel-validation-of-error-feedback-to-dad439cc93`
Run ID: `browser-webrtc-datachannel-validation-of-error-feedback-to-dad439cc93-20260526T134927326836+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Gossip Top-K Sparse Gradients over WebRTC Mesh: enoch://control-plane/projects/gossip-top-k-sparse-gradients-over-webrtc-mesh-bf740f720dab/runs/gossip-top-k-sparse-gradients-over-webrtc-mesh-bf740f720dab-20260526T030951460555+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

WebRTC datachannels were clean for small browser gossip payloads: all tested runs opened 30/30 directed channels, delivered all messages, and had no ICE errors. The tested EF top-k state-gossip mechanism failed the 20% improvement threshold versus no-EF top-k in 0/5 seeds; mean advantage was 6.24%, and a 300-round check showed only 0.16% advantage.

## Boundaries and scale limits

Single host, one headless Chromium browser process, synthetic vectors, ordered reliable datachannels, no WAN/NAT/mobile/cross-browser stress, no real model training gradients, no large peer-count validation.

## Claim scope

Tier 1 controlled direct browser test: 6-peer headless Chromium WebRTC RTCDataChannel mesh running dense, top-k, and error-feedback top-k state gossip on 128-dimensional synthetic vectors for 120 rounds across five seeds, plus one 300-round bounded check.

## Why it stopped

Direct controlled browser validation met transport requirements but failed the EF top-k mechanism success threshold; this is an early Tier 1 negative for the tested state-compression formulation, not a full rejection of all EF gossip variants.

## Recommended next action

Stop this formulation as no-paper Tier 1 evidence; if continuing, run a bounded deepen test using a conserved delta/mass-transfer EF top-k gossip update over the same browser datachannel harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Browser Datachannel Test of Conserved Delta Error-Feedback Top-K Gossip
- Success threshold: EF conserved delta/mass top-k final RMSE is at least 20% lower than no-EF top-k in at least 4/5 seeds, with all directed datachannels opened, all messages received, no ICE errors, and dense gossip improving over initial RMSE.
- Stop condition: Stop as negative if EF conserved delta/mass top-k fails the 20% RMSE advantage in more than one of five seeds or if browser RTCDataChannel delivery is not clean in the controlled local mesh.

## Evidence references

- Artifact root: `<local-path>/projects/browser-webrtc-datachannel-validation-of-error-feedback-to-dad439cc93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
