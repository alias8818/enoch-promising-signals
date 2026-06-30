# Adaptive Window Prompt Lookup Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-window-prompt-lookup-decoding-4457ece6d415`
Run ID: `adaptive-window-prompt-lookup-decoding-4457ece6d415-20260619T204742199039+0000`

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

- Provider-backed Research Facility batch: hf:MiniMaxAI/MiniMax-M3: enoch://research-facility/provider/hf:MiniMaxAI/MiniMax-M3/de473bf63e78

## What looked useful

Adaptive suffix length is risky because longer matches reduce proposal coverage; adaptive window sizing alone may reduce lookup work without hurting acceptance when using short suffixes.

## Boundaries and scale limits

No transformer model, tokenizer, GPU kernel, KV cache, batching, natural corpus, or wall-clock serving path was tested; speedup is verifier-step proxy only.

## Claim scope

Synthetic prompt-lookup decoding proxy over exact-copy, noisy-copy, and low-repeat token streams: longest-suffix adaptive n-gram/window selection underperformed a static 2-gram baseline, while fixed-2-gram adaptive window sizing matched the static 2-gram speedup proxy with much smaller average lookup windows.

## Why it stopped

Proxy/early falsification for longest-suffix adaptive PLD, plus a narrower useful signal for adaptive window sizing; not a full validation.

## Recommended next action

Stop this run as no-paper proxy evidence; next bounded action is to test fixed-2-gram adaptive windows inside a real PLD/speculative decoding implementation on natural prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model fixed-2-gram adaptive-window prompt lookup decoding
- Success threshold: Adaptive-window fixed-2-gram PLD must match static n=2 verifier-step acceptance within 2% while reducing measured lookup overhead by at least 25% and improving or preserving end-to-end tokens/sec on repeated-prompt workloads.
- Stop condition: Stop if adaptive windows reduce acceptance or tokens/sec by more than 2% versus static n=2, or if lookup overhead is too small to yield at least 5% end-to-end latency impact on the chosen stack.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-window-prompt-lookup-decoding-4457ece6d415`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
