# Prompt+KV Suffix-Automaton N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-kv-suffix-automaton-n-gram-speculative-decoding-6e9005865c96`
Run ID: `prompt-kv-suffix-automaton-n-gram-speculative-decoding-6e9005865c96-20260630T103803235906+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e3b49e3a046a

## What looked useful

Online suffix-automaton memory improved verifier-call reduction from 7.83% to 10.21% on tiny_shakespeare and from 10.29% to 11.51% on pride_prejudice. Proposed-token accept rates stayed low at 3.12% and 3.55%, so the mechanism is promising only as a component, not as a standalone paper result.

## Boundaries and scale limits

No transformer verifier, no real KV tensors, no GPU serving latency, no model sampling distribution, and only two public text streams were tested. This is retrieval-mechanism evidence, not production speculative-decoding evidence.

## Claim scope

In a two-dataset oracle text-trace proxy with 20k prompt tokens, 20k evaluation tokens, and max draft length 4, an online prompt+KV-like suffix automaton improved verifier-call reduction over a prompt-only suffix automaton and was competitive with a prompt-only n-gram continuation table.

## Why it stopped

Stopped after a successful bounded proxy: evidence is useful but not paper-grade because it does not include a real transformer verifier or serving latency.

## Recommended next action

Run one bounded direct small-LM validation with a GPT-2-small-class verifier, real generated prompts, and wall-clock tokens/s against prompt-only n-gram and no-drafter controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Direct Validation of Online Suffix-Automaton Drafting
- Success threshold: Online suffix automaton achieves at least 8% wall-clock decoding throughput improvement over no drafter and at least 3% over prompt-only n-gram on the same prompts without increasing peak memory by more than 10%.
- Stop condition: Stop as negative if online suffix automaton fails to beat no-drafter wall-clock throughput by 5% or has lower throughput than prompt-only n-gram on two independent prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-kv-suffix-automaton-n-gram-speculative-decoding-6e9005865c96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
