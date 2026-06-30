# CPU N-gram Draft Engine for Zero-VRAM Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-engine-for-zero-vram-speculation-ba397cab9152`
Run ID: `cpu-n-gram-draft-engine-for-zero-vram-speculation-ba397cab9152-20260609T073325305781+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84b358ff9516

## What looked useful

CPU n-gram drafting is not obviously dead: exact-token acceptance persisted from 24 to 96 prompts, CPU draft cost was sub-20 ms total for 14,990 proposals, and table sizes were about 1.3k entries per prompt. The high zero-accept burst rate means real speedup still depends on verifier efficiency.

## Boundaries and scale limits

No production verifier integration, no end-to-end latency measurement, no neural draft baseline, no larger model or serving workload validation; result is a bounded mechanism benchmark only.

## Claim scope

On cached GPT-2 greedy continuations for 96 WikiText-2 prompts, a CPU-only prompt/local-context n-gram drafter accepted 59.7% of target tokens at max order 8 and implied 2.16x fewer idealized target verification calls, with negligible CPU draft time and tiny CPU tables.

## Why it stopped

Closed as no-paper useful signal because the run directly tested n-gram acceptance but only proxied speculative-decoding speedup; full validation requires target-side block verification and latency measurement.

## Recommended next action

Run a bounded integrated verifier experiment that measures wall-clock latency versus greedy decoding and a small neural draft baseline on the same GPT-2/WikiText-2 setup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated CPU N-gram Speculative Verifier Benchmark
- Success threshold: At least 1.2x end-to-end tokens/s improvement over greedy decoding on 64 or more WikiText-2 prompts without increasing GPU memory by more than verifier-cache overhead.
- Stop condition: Stop if integrated latency is not improved after matching prompts and target settings, or if verifier overhead consumes the idealized call-reduction benefit.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-engine-for-zero-vram-speculation-ba397cab9152`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
