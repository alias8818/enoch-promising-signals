# CPU-Only Evidence-Ledger Agent Loop for Reliable Tool Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-only-evidence-ledger-agent-loop-for-reliable-tool-use-b0192966d3de`
Run ID: `cpu-only-evidence-ledger-agent-loop-for-reliable-tool-use-b0192966d3de-20260605T091009588692+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/b1e4707ceeb8

## What looked useful

At read noise 0.12 over 5,000 episodes, baseline success was 0.7724 with unsupported final claim rate 0.2276; ledger-only success was 0.8718 with unsupported rate 0.1282; ledger+verification/retry success was 0.9930 with unsupported rate 0.0070 and mean tool calls 5.1512 versus 5.0000 baseline. Sensitivity sweeps at noise 0.06, 0.12, and 0.20 preserved the same ordering, while the zero-noise control made all policies perfect.

## Boundaries and scale limits

Synthetic tasks only; no real LLM, real external tools, benchmark suites, adversarial tool outputs, long-context pressure, concurrent tool use, or production traces were tested. The verifier has exact access to structured evidence records.

## Claim scope

In a CPU-only synthetic multi-lookup task harness with injected observation-read/final-composition noise, a structured evidence ledger with final-answer validation and up to two retries improved correctness and reduced unsupported final claims versus an unstructured scratchpad baseline.

## Why it stopped

No-paper closure: the result is useful synthetic mechanism evidence, not direct real-agent or publication-grade validation.

## Recommended next action

Run a bounded real LLM/tool-use benchmark with the same baseline, ledger-only, and ledger+verify policies; stop unless ledger+verify reduces unsupported final answers by at least 30% relative without more than 25% extra tool calls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Tool-Use Benchmark for Evidence-Ledger Verification
- Success threshold: At least 30% relative reduction in unsupported final answers versus baseline, no statistically obvious correctness regression, and mean tool calls no more than 1.25x baseline.
- Stop condition: Stop as negative if ledger+verify fails to reduce unsupported final answers by 30% relative or requires more than 1.25x mean tool calls on the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-only-evidence-ledger-agent-loop-for-reliable-tool-use-b0192966d3de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
