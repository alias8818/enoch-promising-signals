# CPU-Only N-Gram Speculative Decoding Cascade on cpu-proxmox-1

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-only-n-gram-speculative-decoding-cascade-on-cpu-proxmox-1-93b47bc6140e`
Run ID: `cpu-only-n-gram-speculative-decoding-cascade-on-cpu-proxmox-1-93b47bc6140e-20260629T164012664990+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64cd9e1e824e

## What looked useful

Cascade acceptance was 0.998 on synthetic logs, 0.980 on synthetic code, and 0.422 on local docs, versus 0.279, 0.413, and 0.133 for a bigram-only control. Break-even verifier marginal-cost thresholds improved from 0.238/0.352/0.114 to 0.850/0.837/0.359 with zero greedy-equivalence mismatches.

## Boundaries and scale limits

No real transformer verifier was run. Wall-clock speedup was not demonstrated; the Python n-gram harness itself is slower than greedy. The result only supports the n-gram cascade drafting mechanism and cost-threshold analysis.

## Claim scope

Bounded CPU-only n-gram proxy: an order-6 n-gram verifier with a lower-order count-threshold draft cascade exactly preserves greedy output and improves acceptance and verifier break-even cost thresholds versus a bigram-only draft on repetitive synthetic logs/code and local documentation text.

## Why it stopped

The result is a proxy mechanism test rather than full validation; it does not demonstrate real transformer tokens/sec speedup.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded direct test should use a small real CPU transformer verifier with KV-cache greedy decoding, batched candidate verification, and the same bigram control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer Verification for N-Gram Speculative Cascade
- Success threshold: At least 1.15x real tokens/sec over greedy on repetitive text with zero equivalence mismatches, and no worse than 0.95x on non-repetitive text; cascade must outperform bigram-only control.
- Stop condition: Stop if batched verification marginal CPU cost is above the measured break-even threshold or if exact greedy equivalence cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-only-n-gram-speculative-decoding-cascade-on-cpu-proxmox-1-93b47bc6140e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
