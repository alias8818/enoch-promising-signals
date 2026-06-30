# NGramSpeculativeCPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ngramspeculativecpu-e7d61ead48dd`
Run ID: `ngramspeculativecpu-e7d61ead48dd-20260523T163724753440+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d1f0bf117fed

## What looked useful

The mechanism is conditionally supported: target-call reduction alone is insufficient. With a cheap target, speculative decoding was slower (best 0.743x, median 0.257x in the no-overhead sweep). With simulated per-call CPU overhead, median speedup rose above 1x and best speedup reached 8.328x while exact greedy-output equivalence was maintained.

## Boundaries and scale limits

No real transformer, KV cache, tokenizer, ONNX Runtime, llama.cpp, or production CPU inference kernel was tested; corpora and prompts are small in-repo fixtures; fixed target-call overhead is simulated CPU work.

## Claim scope

Bounded pure-Python proxy: a history n-gram drafter can preserve exact greedy output and reduce target calls by up to 87.5% on repetitive/patterned n-gram target-model prompts, but wall-clock gains appear only when target calls have enough fixed CPU cost to amortize drafting and verification overhead.

## Why it stopped

Closed as no-paper useful signal because the evidence is proxy-only: it validates the mechanism and threshold condition, but not real CPU transformer serving.

## Recommended next action

Run a bounded real-model CPU follow-up using the same exact-output checks around a small transformer or llama.cpp/ONNX Runtime target, and stop unless it beats greedy latency on repeated-context prompts without changing generated tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer N-Gram Speculative Decoding Probe
- Success threshold: On a real CPU transformer target, achieve at least 1.2x median latency speedup versus greedy on repeated-context prompts with exact output equality, while not regressing the low-repeat control by more than 10%.
- Stop condition: Stop as negative if exact-output speculative decoding is slower than greedy on repeated-context prompts for all draft settings, or if maintaining exact greedy equivalence requires changes that remove the target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/ngramspeculativecpu-e7d61ead48dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
