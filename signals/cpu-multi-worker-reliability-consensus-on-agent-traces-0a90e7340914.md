# CPU Multi-Worker Reliability Consensus on Agent Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-multi-worker-reliability-consensus-on-agent-traces-0a90e7340914`
Run ID: `cpu-multi-worker-reliability-consensus-on-agent-traces-0a90e7340914-20260628T224550055374+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/edbe5c5bae6d

## What looked useful

Consensus is conditionally useful: it beat the best worker by +0.052200 mean accuracy under independent worker noise, but trailed the best worker by -0.029533 mean accuracy under correlated blind spots. This supports adding diversity diagnostics or specialist routing before relying on consensus as a reliability mechanism.

## Boundaries and scale limits

Synthetic traces only; no real Enoch traces, real LLM worker judgments, human adjudication, latency/cost accounting, or production-scale workload were tested.

## Claim scope

In a deterministic synthetic agent-trace benchmark, majority consensus improved reliability when worker errors were independent and complementary, but lost to the best specialist when workers shared a correlated blind spot.

## Why it stopped

Synthetic/proxy evidence is useful for mechanism design but insufficient for publication-grade or production reliability claims.

## Recommended next action

Run a bounded real-trace deepen test with adjudicated labels, fixed worker prompts/models, and explicit diversity diagnostics; stop this synthetic run as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace multi-worker consensus reliability with diversity diagnostics
- Success threshold: Consensus beats the best single worker by at least +0.03 accuracy with a positive bootstrap p05 in the low-correlation subset, and fails or routes away in a high-correlation subset without degrading below the best worker by more than -0.01.
- Stop condition: Stop as negative if consensus does not beat the best worker in the low-correlation real-trace subset, or if diversity diagnostics cannot separate helpful from harmful consensus regimes.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-multi-worker-reliability-consensus-on-agent-traces-0a90e7340914`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
