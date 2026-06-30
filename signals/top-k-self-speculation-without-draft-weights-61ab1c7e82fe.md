# Top-k Self-Speculation Without Draft Weights

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `top-k-self-speculation-without-draft-weights-61ab1c7e82fe`
Run ID: `top-k-self-speculation-without-draft-weights-61ab1c7e82fe-20260621T213642070456+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3cfee0d59dca

## What looked useful

The current target top-k list was sufficient for the immediate greedy token but did not provide enough conditional information for longer speculative windows. Best call-count condition accepted 2.016 tokens/call but used 1.984x target-position work; the best token-work condition was break-even at 1.000x.

## Boundaries and scale limits

No neural Transformer, GPU latency, KV-cache behavior, or benchmark corpus was tested. The result should not be read as a full-scale validation or universal impossibility proof.

## Claim scope

Bounded proxy on an exact character 5-gram target model: top-k-only self-speculation without draft weights did not reduce target-position work versus greedy decoding, despite reducing serial verification calls in the best cases.

## Why it stopped

Proxy early falsification of the compute-saving version of the hypothesis: call-count savings did not translate into target-position work reduction in the bounded exact-decoding test.

## Recommended next action

Stop this run as a proxy useful-signal negative; the concrete next step is a small neural LM acceptance and latency benchmark that accounts for verification-window target work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural LM latency check for top-k-only self-speculation
- Success threshold: At least 10% measured latency/token improvement versus greedy with target-position work multiplier no worse than 1.05 and exact output equivalence.
- Stop condition: Stop if draft length 2 fails to improve measured latency/token by 10% or if longer draft windows require more than 1.05x target-position work without compensating latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-self-speculation-without-draft-weights-61ab1c7e82fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
