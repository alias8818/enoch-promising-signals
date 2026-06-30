# Tiny Suffix Draft for Speculative Decoding on One GPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-suffix-draft-for-speculative-decoding-on-one-gpu-59694c3aba49`
Run ID: `tiny-suffix-draft-for-speculative-decoding-on-one-gpu-59694c3aba49-20260529T235752042787+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3f2524755b31

## What looked useful

Short suffix keys hit generated contexts often but had very low acceptance: suffix len 1 hit 79.0% of generated-token positions but accepted only 1.91% of drafted tokens and slowed wall-clock to 0.954x. Longer keys improved precision but almost never hit; suffix len 4 hit 1.6% of positions and still slowed to 0.989x. The failure mode is corpus-frequency suffix mismatch, not lookup overhead.

## Boundaries and scale limits

Tested GPT-2 only, 14 evaluable WikiText prompts, 32 generated tokens per prompt, unbatched greedy decoding, suffix table draft rather than a learned neural draft, and short local runs rather than production serving.

## Claim scope

On a single NVIDIA GB10 GPU, a tiny raw suffix n-gram table used as a 4-token speculative draft for GPT-2 greedy decoding did not improve latency or meaningfully reduce target calls versus target-only KV-cache greedy decoding.

## Why it stopped

Early bounded falsification: direct one-GPU GPT-2 evidence showed exact speculative decoding with the tiny raw suffix table was slower than baseline and reduced target calls by at most 1.3%, so it does not justify paper writing or larger validation in this form.

## Recommended next action

Stop this raw suffix-table approach as a no-paper negative; the only bounded next test worth running is a target-generated suffix draft that measures whether conditioning the table on model continuations can clear a 10% target-call reduction threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Target-Generated Tiny Suffix Draft Upper Bound
- Success threshold: Exact greedy output agreement plus at least 10% target-call reduction and at least 1.05x wall-clock speedup on GPT-2-class one-GPU decoding under the same prompt/token budget.
- Stop condition: Stop if target-generated suffix conditioning still gives less than 5% target-call reduction or fails exact output agreement in fp32.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-suffix-draft-for-speculative-decoding-on-one-gpu-59694c3aba49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
