# Deep-model Merkle spot-check gradient verification overhead

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deep-model-merkle-spot-check-gradient-verification-overhea-684a45e57c`
Run ID: `deep-model-merkle-spot-check-gradient-verification-overhea-684a45e57c-20260629T122215396933+0000`

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

- Parent run decision: Merkle-Commitment Spot-Check Gradient Verification: enoch://control-plane/projects/merkle-commitment-spot-check-gradient-verification-03b9cecb138b/runs/merkle-commitment-spot-check-gradient-verification-03b9cecb138b-20260629T120555379729+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4aed25db8fa9

## What looked useful

Full-gradient Merkle commitment is dominated by CPU gradient copy/leaf hashing, not by Merkle proof verification. Larger chunks reduce tree-build cost but do not make the naive design practical because hashing every gradient byte still adds roughly 120-150 ms for a 33.3M parameter model.

## Boundaries and scale limits

Synthetic MLPs only; no transformer/GPT-2-small workload, no distributed adversary, no network protocol, no optimizer-state commitments, no GPU-resident hashing, and no asynchronous overlap. The result falsifies only the naive synchronous CPU full-gradient commitment design as a low-overhead per-step primitive in this local setting.

## Claim scope

On synthetic 4-32 layer MLP GPU training loops up to 33.3M parameters on NVIDIA GB10, naive per-step full-gradient CPU BLAKE2b Merkle commitment costs 5.9x-9.3x the baseline training step for ordinary 128-256 spot-check counts, while proof verification alone is about 0.12-1.31 ms for 32-256 checks and about 21.19 ms for 4096 checks.

## Why it stopped

Bounded local evidence is sufficient for a no-paper useful signal: the naive synchronous CPU full-gradient Merkle commitment path is an early practical falsification, not a full validation of all possible Merkle verification designs.

## Recommended next action

Run a bounded deepen test that implements GPU-resident or overlapped gradient commitment on a GPT-2-small-class training loop and stop if total verification overhead remains above 25% for 256 spot checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU-resident Merkle gradient commitment on GPT-2-small-class training
- Success threshold: Total commitment plus 256 proof verifications adds <=25% mean wall-clock overhead versus baseline training for at least 100 measured steps, with all injected sampled tamper events detected.
- Stop condition: Stop as a practical negative if overhead remains >25% after GPU-resident or overlapped commitment, or if implementation requires non-local datacenter resources before producing a 100-step bounded measurement.

## Evidence references

- Artifact root: `<local-path>/projects/deep-model-merkle-spot-check-gradient-verification-overhea-684a45e57c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
