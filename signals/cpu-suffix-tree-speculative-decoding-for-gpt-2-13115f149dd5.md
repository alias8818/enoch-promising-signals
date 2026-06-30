# CPU suffix-tree speculative decoding for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-suffix-tree-speculative-decoding-for-gpt-2-13115f149dd5`
Run ID: `cpu-suffix-tree-speculative-decoding-for-gpt-2-13115f149dd5-20260523T072414752440+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4041ebcdf4b0

## What looked useful

Suffix lookup accepted 32/32 proposed tokens and gave 2.06x-2.24x wall speedups on two repetitive prompts, but on the four-prompt exact benchmark it accepted only 93/208 proposed tokens and slowed aggregate wall time to 0.68x despite reducing target forward calls by 47.7%.

## Boundaries and scale limits

Only 4 hand-authored prompts, 32 generated tokens per prompt, greedy decoding only, GPT-2-small only, simple suffix scan instead of an optimized suffix tree, and no production prompt corpus. Cached multi-token verification was attempted but did not preserve exact greedy output on natural/code-like prompts.

## Claim scope

On GPT-2-small greedy CPU decoding with four short prompts, prompt/history suffix lookup exactly accelerates highly repetitive prompts but slows the mixed prompt set when using a conservative exact full-context verifier.

## Why it stopped

Bounded direct GPT-2 CPU evidence is mixed: strong on repeated prompts but not a general acceleration result, and the cached verifier path failed exactness.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded work should first implement and unit-test an exact cached verifier before evaluating a repetition-gated suffix lookup on a real prompt corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact cached verifier and repetition-gated suffix lookup for GPT-2 CPU decoding
- Success threshold: Exact match with greedy on all tested prompts and at least 1.15x aggregate CPU wall speedup over cached greedy on a mixed prompt set of at least 100 prompts.
- Stop condition: Stop if exact cached verification cannot be made equivalent to full-context logits, or if the gated method is below 1.0x aggregate wall speed after 100 mixed prompts.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-tree-speculative-decoding-for-gpt-2-13115f149dd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
