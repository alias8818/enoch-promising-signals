# Prompt-Lookup Speculative Decoding for VRAM-Free Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-speculative-decoding-for-vram-free-drafting-ea7f49c21223`
Run ID: `prompt-lookup-speculative-decoding-for-vram-free-drafting-ea7f49c21223-20260525T123620979621+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31aa1832cda5

## What looked useful

Wikitext corpus probe accepted only 77 of 3456 future tokens (2.23%), reducing target evaluations by 0.81% for a 1.008x oracle speedup bound. A repetitive prompt produced 4.36x median wall-clock speedup on GPT-2, but Hugging Face prompt lookup overshot max_new_tokens and one natural-text control diverged within the requested overlap.

## Boundaries and scale limits

Tested GPT-2 only, Wikitext-2 only for the corpus probe, five natural-text generation prompts, and a deliberately repetitive prompt control. Did not test larger models, code/RAG/chat workloads, batching, long-context production serving, or a custom exact verifier.

## Claim scope

Bounded local evidence on GPT-2/Wikitext-2 and repetitive prompts: prompt lookup can accelerate highly repetitive greedy generation without a second draft model, but ordinary Wikitext continuation has too few reusable spans to produce meaningful target-call reduction.

## Why it stopped

Bounded direct evidence is mixed: the mechanism works on repetitive prompts but is effectively negligible on ordinary Wikitext and the observed library path has correctness/length caveats.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test exact prompt-lookup verification on naturally repetitive code/RAG/document-edit workloads with a strict no-drift and no-overshoot success gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact Prompt-Lookup Drafting on Naturally Repetitive Code and RAG Contexts
- Success threshold: Median target-call reduction >=15%, median wall-clock speedup >=1.15x, and 100% exact output identity on the requested token budget for at least one naturally repetitive workload.
- Stop condition: Stop if accepted draft-token fraction remains below 5% or any verified run shows token drift/length overshoot after implementation fixes.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculative-decoding-for-vram-free-drafting-ea7f49c21223`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
