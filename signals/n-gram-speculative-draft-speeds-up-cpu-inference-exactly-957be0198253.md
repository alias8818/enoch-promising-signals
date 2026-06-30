# N-gram speculative draft speeds up CPU inference exactly

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-speeds-up-cpu-inference-exactly-957be0198253`
Run ID: `n-gram-speculative-draft-speeds-up-cpu-inference-exactly-957be0198253-20260529T170724290868+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5be7df449ccc

## What looked useful

N-gram speculative drafting can be exact and faster on CPU when draft acceptance is high; the speedup disappears on uncovered prompts, making coverage/acceptance the key condition.

## Boundaries and scale limits

This run did not use a real transformer/LLM runtime, KV cache, sampled decoding, or natural prompt corpus. The n-gram table was trained on target-generated sequences, and random prompts showed no acceleration. Results are mechanism evidence, not broad CPU inference validation.

## Claim scope

In a deterministic NumPy CPU toy LM, exact greedy speculative decoding with a corpus-derived n-gram draft speeds up generation when prompts are covered by the n-gram table; across three seeds, in-domain speedup was 1.74x at gamma 4, 2.52x at gamma 8, and 3.22x at gamma 16, with exact output equality.

## Why it stopped

Bounded toy evidence supports exact in-domain speedup but not the broad claim that n-gram speculative drafts speed up CPU inference generally; random uncovered prompts were neutral to slightly slower.

## Recommended next action

Stop as no-paper useful signal; the concrete next test is a bounded real-LLM CPU benchmark using llama.cpp prompt-lookup or equivalent n-gram speculative decoding on a realistic repetitive corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM CPU n-gram speculative decoding on repetitive prompts
- Success threshold: At least 1.2x aggregate tokens/sec improvement with exact greedy output equality on the high-coverage corpus, and clear reporting of low-coverage control behavior.
- Stop condition: Stop if a real LLM runtime cannot show at least 1.1x speedup on high-coverage prompts or if exact output equality fails.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-speeds-up-cpu-inference-exactly-957be0198253`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
