# CPU speculative decoding with exact n-gram suffix drafter

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-speculative-decoding-with-exact-n-gram-suffix-drafter-04f9adb71ba3`
Run ID: `cpu-speculative-decoding-with-exact-n-gram-suffix-drafter-04f9adb71ba3-20260613T092742324119+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bb53858795a

## What looked useful

Exact suffix drafting can substantially reduce ideal verifier calls on repetitive/boilerplate traces (best synthetic 0.932940 reduction; best local natural/project trace 0.444759) but offers little or no benefit on low-repeat traces, so it is a niche recurrence exploit rather than a general semantic drafter.

## Boundaries and scale limits

No real CPU language model verifier, no production tokenizer, no KV-cache integration, no large natural corpus, and no end-to-end decoding wall-clock benchmark.

## Claim scope

Offline trace-level evaluation of an online exact n-gram suffix drafter on local project texts and synthetic controls shows verifier-call reductions when exact suffix continuations recur.

## Why it stopped

No-paper closure: this run produced a bounded trace-level useful signal, but not direct full CPU decoding validation.

## Recommended next action

Run a bounded direct CPU LM integration with a small native-tokenizer model and compare wall-clock tokens/s plus exact output equivalence against plain greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LM benchmark for exact suffix speculative drafting
- Success threshold: At least 15% wall-clock tokens/s improvement on repetitive prompts with exact output equivalence and no more than 5% slowdown on low-repeat controls.
- Stop condition: Stop if model integration cannot show both exact output equivalence and a positive wall-clock gain on repetitive prompts within a bounded CPU run.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-with-exact-n-gram-suffix-drafter-04f9adb71ba3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
